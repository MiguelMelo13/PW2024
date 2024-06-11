from django.contrib import admin
from .models import User, Author, Article, Comment, Rating, Category, Follow

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'nationality', 'date_joined','comment_count')
    search_fields = ('username', 'first_name', 'last_name', 'nationality')
    list_filter = ('date_joined',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'nationality', 'author_followers','author_rating')
    search_fields = ('username', 'first_name', 'last_name', 'nationality')
    list_filter = ('date_joined',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','average_rating', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'created_at')
    search_fields = ('article__title', 'user__username')
    list_filter = ('created_at',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'value')
    search_fields = ('article__title', 'user__username')
    list_filter = ('value',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','article_count')
    search_fields = ('name',)

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    search_fields = ('user__username', 'author__username')
