from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index_view, name='index'),

    path('article/<int:article_id>/', views.article_detail_view, name='article_detail'),
    path('author/<int:author_id>/', views.author_detail_view, name='author_detail'),
    path('category/<int:category_id>/', views.category_detail_view, name='category_detail'),
    path('user/<int:user_id>/', views.user_detail_view, name='user_detail'),

    path('authors_list/', views.authors_list_view, name='authors_list'),
    path('categories_list/', views.categories_list_view, name='categories_list'),
    path('articles_list/', views.articles_list_view, name='articles_list'),
    path('add_article/', views.add_article_view, name='add_article'),


    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
