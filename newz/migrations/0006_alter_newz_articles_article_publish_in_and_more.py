# Generated by Django 4.1.4 on 2023-01-11 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newz', '0005_alter_newz_articles_article_publish_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newz_articles',
            name='article_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 1, 44, 51, 883668)),
        ),
        migrations.AlterField(
            model_name='newz_categories',
            name='category_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 1, 44, 51, 883668)),
        ),
    ]
