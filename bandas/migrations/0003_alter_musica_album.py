# Generated by Django 4.0.6 on 2024-04-09 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_album_genero_musical_album_numero_faixas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.album'),
        ),
    ]
