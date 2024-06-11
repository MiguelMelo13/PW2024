from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re
from .models import User, Author, Category, Article, Follow, Rating, Comment
from .forms import ArticleForm, CommentForm, RatingForm, RegistrationForm

def index_view(request):

    featured_articles = Article.objects.filter(is_featured=True)[:3]
    latest_articles = Article.objects.order_by('-created_at')[:5]
    return render(request, 'wrongOpinions/index.html', {
        'featured_articles': featured_articles,
        'latest_articles': latest_articles
    })


def authors_list_view(request):
    authors = Author.objects.all()
    return render(request, 'wrongOpinions/author_list.html', {'authors': authors})

def categories_list_view(request):
    categories = Category.objects.all()
    return render(request, 'wrongOpinions/category_list.html', {'categories': categories})

def articles_list_view(request):
    articles = Article.objects.all()
    return render(request, 'wrongOpinions/article_list.html', {'articles': articles})


def author_detail_view(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'wrongOpinions/author.html', {'author': author})

def category_detail_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'wrongOpinions/category.html', {'category': category})

def article_detail_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()
    rating = None
    if request.user.is_authenticated:
        try:
            rating = Rating.objects.get(article=article, user=request.user)
        except Rating.DoesNotExist:
            rating = None

    if request.method == 'POST':
        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.article = article
                comment.save()
                messages.success(request, 'Your comment has been added.')
                return redirect('article_detail', article_id=article.id)
        elif 'rating' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                if rating is None:
                    rating = rating_form.save(commit=False)
                    rating.user = request.user
                    rating.article = article
                    rating.save()
                else:
                    rating.value = rating_form.cleaned_data['value']
                    rating.save()
                messages.success(request, 'Your rating has been submitted.')
                return redirect('article_detail', article_id=article.id)
    else:
        comment_form = CommentForm()
        rating_form = RatingForm(instance=rating)

    return render(request, 'wrongOpinions/article.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'rating': rating,
    })

from django.shortcuts import render, get_object_or_404
from .models import User

def user_detail_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    comments = user.comment_set.select_related('article')
    followed_authors = user.followed_authors.all()

    context = {
        'user': user,
        'comments': comments,
        'followed_authors': followed_authors,
    }
    return render(request, 'wrongOpinions/user.html', context)



def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if 'bio' in request.POST:  # Check if the form is for registering an author
                author = form.save(commit=False)
                author.is_author = True
                author.save()
            else:  # Otherwise, register a regular user
                user = form.save()
                login(request, user)
                return redirect('home')  # Redirect to home after registration
    else:
        form = RegistrationForm()
    return render(request, 'wrongOpinions/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a success page.
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to login page on failure.

    return render(request, 'wrongOpinions/login.html')

def logout_view(request):
    logout(request)
    return redirect('index') 


@login_required
def apaga_autor_view(request, autor_id):
    autor = Author.objects.get(id=autor_id)
    autor.delete()
    return redirect('autores')

@login_required
def add_article_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            messages.success(request, 'Article created successfully.')
            return redirect('articles_list')  # Replace with your article list view name
    else:
        form = ArticleForm()
    return render(request, 'wrongOpinions/add_article.html', {'form': form})