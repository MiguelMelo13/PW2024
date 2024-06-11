from django.db import models
from django.utils.html import format_html

from django.db.models import Count, Avg

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    profilePic = models.ImageField(upload_to='images/', null=True, blank=True)
    nationality = models.CharField(max_length=25)
    comment_count = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50, unique=True)
    followed_authors = models.ManyToManyField('Author', related_name='followers_relationships', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.pk:
            for author in self.followed_authors.all():
                Follow.objects.get_or_create(user=self, author=author)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Author(User):
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    author_followers = models.IntegerField(default=0)
    verification_status = models.BooleanField(default=False)
    author_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name='Rating')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    @property
    def article_count(self):
        return self.articles.count()

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    core_text = models.TextField()
    cover_image = models.ImageField(upload_to='article_covers/')
    complementary_images = models.ImageField(upload_to='article_complementary/', blank=True, null=True, max_length=3)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def average_rating(self):
        avg_rating = self.rating_set.aggregate(avg_rating=Avg('value'))['avg_rating']
        if avg_rating is not None:
            return round(avg_rating, 1)
        return None

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.user.comment_count = Comment.objects.filter(user=self.user).count()
        self.user.save()


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        author = self.article.author
        ratings = Rating.objects.filter(article__author=author)
        avg_rating = ratings.aggregate(avg_rating=Avg('value'))['avg_rating']
        author.author_rating = avg_rating if avg_rating is not None else 0
        author.save()




class Follow(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='following_relationships')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='follower_relationships')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.author.author_followers = self.author.follower_relationships.count()
        self.author.save()


