# Generated by Django 4.0.6 on 2024-06-10 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0003_alter_musica_album'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'permissions': [('change_album_permission', 'Can change album'), ('delete_album_permission', 'Can delete album')]},
        ),
        migrations.AlterModelOptions(
            name='banda',
            options={'permissions': [('change_banda_permission', 'Can change banda'), ('delete_banda_permission', 'Can delete banda')]},
        ),
        migrations.AlterModelOptions(
            name='musica',
            options={'permissions': [('change_musica_permission', 'Can change musica'), ('delete_musica_permission', 'Can delete musica')]},
        ),
    ]