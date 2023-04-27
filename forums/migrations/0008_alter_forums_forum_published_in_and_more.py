# Generated by Django 4.1.4 on 2023-02-03 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0007_alter_forums_forum_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forums',
            name='forum_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 6, 47, 17, 266632)),
        ),
        migrations.AlterField(
            model_name='forums_comments',
            name='comment_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 6, 47, 17, 274654)),
        ),
        migrations.AlterField(
            model_name='forums_posts',
            name='post_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 6, 47, 17, 274654)),
        ),
        migrations.AlterField(
            model_name='forums_replies',
            name='reply_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 6, 47, 17, 274654)),
        ),
    ]
