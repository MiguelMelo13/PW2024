# forms.py
from django import forms
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nome', 'foto', 'biografia', 'ano', 'genero_musical', 'nacionalidade']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'capa', 'banda', 'ano_lancamento', 'genero_musical', 'produtor', 'numero_faixas']

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'album', 'spotify_link', 'duracao_minutos', 'letra', 'data_lancamento']
