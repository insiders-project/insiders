# Generated by Django 4.1.4 on 2023-01-25 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newz', '0025_alter_newz_articles_article_publish_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newz_articles',
            name='article_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 25, 18, 51, 36, 853934)),
        ),
        migrations.AlterField(
            model_name='newz_categories',
            name='category_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 25, 18, 51, 36, 853934)),
        ),
    ]
