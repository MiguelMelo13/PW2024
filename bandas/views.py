# bandas/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Banda,Album,Musica
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def layout_view(request):
    return render(request, "bandas/layout.html")

def lista_layout_view(request):
    return render(request, "bandas/lista_layout.html")

def index_view(request):

    bandas = Banda.objects.all()
    albuns = Album.objects.all()

    lista_bandas = [banda.nome for banda in bandas]
    lista_albuns = [album.titulo for album in albuns]

    context = {
        'bandas' : lista_bandas,
        'albuns' : lista_albuns
    }


    return render(request, "bandas/index.html", context)

def bandaX_view(request, banda_id):
    # Obter a instância da banda pelo ID
    banda = get_object_or_404(Banda, id=banda_id)

    # Filtrar os álbuns da banda pelo nome da banda
    albuns_banda = Album.objects.filter(banda__nome=banda.nome)

    # Criar o contexto para passar para o template
    context = {
        'banda': banda,
        'albuns_banda': albuns_banda  # Álbuns filtrados da banda pelo nome
    }

    # Renderizar o template banda.html com o contexto
    return render(request, 'bandas/banda.html', context)


def albumX_view(request, album_id):

    context = {'album': Album.objects.get(id=album_id)}

    return render(request, "bandas/album.html", context)


def musicaX_view(request, musica_id):

    context = {'musica': Musica.objects.get(id=musica_id)}

    return render(request, "bandas/musica.html", context)



def lista_bandas_view(request):

    context = {'bandas_list': Banda.objects.all()}

    return render(request, "bandas/lista_bandas.html", context)

def lista_albuns_view(request):
    albums_list = Album.objects.all()  # Retrieve all albums from the database
    context = {'albums_list': albums_list}  # Pass the albums list to the template context
    return render(request, 'bandas/lista_albuns.html', context)

def lista_musicas_view(request):

    context = {'musicas_list': Musica.objects.all()}

    return render(request, "bandas/lista_musicas.html", context)
# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('bandas:index')  # Replace 'home' with your desired redirect URL
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'bandas/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('bandas:index')


def nova_banda_view(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/bandas/lista_bandas')  # Redirect to a list view of bands
    else:
        form = BandaForm()
    return render(request, 'bandas/nova_banda.html', {'form': form})

def novo_album_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_albuns')  # Redirect to a list view of albums
    else:
        form = AlbumForm()
    return render(request, 'bandas/novo_album.html', {'form': form})

def nova_musica_view(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_musicas')  # Redirect to a list view of musicas
    else:
        form = MusicaForm()
    return render(request, 'bandas/nova_musica.html', {'form': form})




def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        # Add logic to delete the album...
        album.delete()
        return redirect('bandas:lista_albuns')
    # Redirect to some page if the request method is not POST
    return redirect('bandas:lista_albuns')


@require_POST
def delete_album_view(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
        # Perform any additional permission checks here if needed

        # Delete the album
        album.delete()

        return JsonResponse({'message': 'Album deleted successfully'}, status=200)
    except Album.DoesNotExist:
        return JsonResponse({'error': 'Album not found'}, status=404)


@require_POST
def delete_banda_view(request, banda_id):
    try:
        banda = Banda.objects.get(pk=banda_id)
        # Perform any additional permission checks here if needed

        # Delete the banda
        banda.delete()

        return JsonResponse({'message': 'Banda deleted successfully'}, status=200)
    except Banda.DoesNotExist:
        return JsonResponse({'error': 'Banda not found'}, status=404)
    
@require_POST
def delete_musica_view(request, musica_id):
    try:
        musica = Musica.objects.get(pk=musica_id)
        # Perform any additional permission checks here if needed

        # Delete the musica
        musica.delete()

        return JsonResponse({'message': 'Musica deleted successfully'}, status=200)
    except Musica.DoesNotExist:
        return JsonResponse({'error': 'Musica not found'}, status=404)
    
def edit_album_view(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:lista_albuns')  # Adjust the redirect as needed
    else:
        form = AlbumForm(instance=album)

    return render(request, 'bandas/edit_album.html', {'form': form})

def edit_musica_view(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)

    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:musicas_list')  # Adjust the redirect as needed
    else:
        form = MusicaForm(instance=musica)

    return render(request, 'bandas/edit_musica.html', {'form': form})

def edit_banda_view(request, banda_id):
    banda = get_object_or_404(Banda, pk=banda_id)

    if request.method == 'POST':
        form = BandaForm(request.POST, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda', banda_id=banda.id)  # Redirect to the band's detail page
    else:
        form = BandaForm(instance=banda)

    return render(request, 'bandas/edit_banda.html', {'form': form, 'banda': banda})
