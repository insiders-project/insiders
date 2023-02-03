# Generated by Django 4.1.4 on 2023-01-31 00:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0005_alter_forums_forum_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forums',
            name='forum_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 3, 32, 35, 906646)),
        ),
        migrations.AlterField(
            model_name='forums_comments',
            name='comment_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 3, 32, 35, 906646)),
        ),
        migrations.AlterField(
            model_name='forums_posts',
            name='post_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 3, 32, 35, 906646)),
        ),
        migrations.CreateModel(
            name='Forums_replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.TextField()),
                ('reply_is_active', models.BooleanField(default=True)),
                ('replyed_by', models.CharField(max_length=50)),
                ('reply_published_in', models.DateTimeField(default=datetime.datetime(2023, 1, 31, 3, 32, 35, 922252))),
                ('reply_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.forums_comments')),
                ('reply_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reply_forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.forums')),
                ('reply_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.forums_posts')),
            ],
        ),
    ]
