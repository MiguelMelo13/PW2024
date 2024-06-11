from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField()
    biografia = models.TextField()
    ano = models.IntegerField()
    genero_musical = models.CharField(max_length=50, blank=True)
    nacionalidade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome

    def get_albums(self):
        return self.album_set.all()

    class Meta:
        permissions = [
            ("change_banda_permission", "Can change banda"),
            ("delete_banda_permission", "Can delete banda"),
        ]

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capas/')
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    ano_lancamento = models.IntegerField()
    genero_musical = models.CharField(max_length=50, blank=True)
    produtor = models.CharField(max_length=100, blank=True)
    numero_faixas = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        permissions = [
            ("change_album_permission", "Can change album"),
            ("delete_album_permission", "Can delete album"),
        ]

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    spotify_link = models.URLField(blank=True, null=True)
    duracao_minutos = models.PositiveIntegerField(blank=True, null=True)
    letra = models.TextField(blank=True)
    data_lancamento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Update numero_faixas for the associated album after saving
        self.album.numero_faixas = self.album.musicas.count()
        self.album.save(update_fields=['numero_faixas'])

    class Meta:
        permissions = [
            ("change_musica_permission", "Can change musica"),
            ("delete_musica_permission", "Can delete musica"),
        ]
