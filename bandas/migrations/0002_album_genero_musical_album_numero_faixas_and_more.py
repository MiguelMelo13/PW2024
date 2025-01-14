# Generated by Django 4.0.6 on 2024-03-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genero_musical',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='album',
            name='numero_faixas',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='produtor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='banda',
            name='genero_musical',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='banda',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='musica',
            name='data_lancamento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='musica',
            name='duracao_minutos',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='musica',
            name='letra',
            field=models.TextField(blank=True),
        ),
    ]
