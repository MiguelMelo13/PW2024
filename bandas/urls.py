# bandas/urls.py

from django.urls import path
from . import views
from .views import * 

app_name = 'bandas'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('layout/', views.layout_view, name='layout'),
    path('lista_layout/', views.lista_layout_view, name='lista_layout'),

    path('banda/<int:banda_id>/', views.bandaX_view, name='banda'),
    path('album/<int:album_id>/', views.albumX_view, name='album'),
    path('musica/<int:musica_id>/', views.musicaX_view, name='musica'),


    path('lista_bandas/', views.lista_bandas_view, name='lista_bandas'),
    path('lista_albuns/', views.lista_albuns_view, name='lista_albuns'),
    path('lista_musicas/', views.lista_musicas_view, name='lista_musicas'),


    path('banda/novo', views.nova_banda_view, name='nova_banda'),
    path('album/novo', views.novo_album_view, name='novo_album'),
    path('musica/novo', views.nova_musica_view, name='nova_musica'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('delete_banda/<int:banda_id>/', views.delete_banda_view, name='delete_banda'),
    path('delete_album/<int:album_id>/', views.delete_album_view, name='delete_banda'),
    path('delete_musica/<int:musica_id>/', views.delete_musica_view, name='delete_musica'),

    path('edit_banda/<int:banda_id>/', views.edit_banda_view, name='edit_banda'),
    path('edit_album/<int:album_id>/', views.edit_album_view, name='edit_album'),
    path('edit_musica/<int:musica_id>/', views.edit_musica_view, name='edit_musica'),
    

]