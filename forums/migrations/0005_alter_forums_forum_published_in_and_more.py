# Generated by Django 4.1.4 on 2023-01-30 19:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0004_remove_forums_posts_forum_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forums',
            name='forum_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 22, 57, 13, 848668)),
        ),
        migrations.AlterField(
            model_name='forums_posts',
            name='post_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 30, 22, 57, 13, 864293)),
        ),
        migrations.CreateModel(
            name='Forums_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('comment_is_active', models.BooleanField(default=True)),
                ('commented_by', models.CharField(max_length=50)),
                ('comment_published_in', models.DateTimeField(default=datetime.datetime(2023, 1, 30, 22, 57, 13, 864293))),
                ('comment_created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.forums')),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forums.forums_posts')),
            ],
        ),
    ]
