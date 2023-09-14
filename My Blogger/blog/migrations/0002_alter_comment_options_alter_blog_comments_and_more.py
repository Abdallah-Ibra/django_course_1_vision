# Generated by Django 4.2 on 2023-09-03 12:44

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='blog_comments', to='blog.comment'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.image_upload),
        ),
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='blog_likes', to='blog.like'),
        ),
    ]