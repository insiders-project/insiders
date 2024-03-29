# Generated by Django 4.1.4 on 2023-02-01 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0006_alter_forums_forum_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forums',
            name='forum_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 1, 10, 8, 25, 344717)),
        ),
        migrations.AlterField(
            model_name='forums_comments',
            name='comment_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 1, 10, 8, 25, 344717)),
        ),
        migrations.AlterField(
            model_name='forums_posts',
            name='post_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 1, 10, 8, 25, 344717)),
        ),
        migrations.AlterField(
            model_name='forums_replies',
            name='reply_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 1, 10, 8, 25, 344717)),
        ),
    ]
