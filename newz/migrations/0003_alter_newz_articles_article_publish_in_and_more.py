# Generated by Django 4.1.4 on 2022-12-30 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newz', '0002_newz_articles_newz_categories_delete_newz_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newz_articles',
            name='article_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 10, 14, 59, 787593)),
        ),
        migrations.AlterField(
            model_name='newz_categories',
            name='category_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 10, 14, 59, 787593)),
        ),
    ]