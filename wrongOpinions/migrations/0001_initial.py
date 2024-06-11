# Generated by Django 4.0.6 on 2024-03-16 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('core_text', models.TextField()),
                ('cover_image', models.ImageField(upload_to='article_covers/')),
                ('complementary_images', models.ImageField(blank=True, max_length=3, null=True, upload_to='article_complementary/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('profilePic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('nationality', models.CharField(max_length=25)),
                ('comment_count', models.IntegerField(default=0)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wrongOpinions.user')),
                ('bio', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('author_followers', models.IntegerField(default=0)),
                ('verification_status', models.BooleanField(default=False)),
                ('author_rating', models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Rating')),
            ],
            bases=('wrongOpinions.user',),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wrongOpinions.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wrongOpinions.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wrongOpinions.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wrongOpinions.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='followed_authors',
            field=models.ManyToManyField(blank=True, related_name='followers', to='wrongOpinions.author'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wrongOpinions.author'),
        ),
    ]