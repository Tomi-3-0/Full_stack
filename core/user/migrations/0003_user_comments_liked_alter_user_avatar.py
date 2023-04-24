# Generated by Django 4.0 on 2023-04-23 21:44

import core.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_comment', '0001_initial'),
        ('core_user', '0002_user_posts_liked_alter_user_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comments_liked',
            field=models.ManyToManyField(related_name='commented_by', to='core_comment.Comment'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=core.user.models.user_directory_path),
        ),
    ]
