# Generated by Django 4.1.4 on 2023-01-12 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_alter_contents_content_publish_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='content_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 20, 50, 2, 938324)),
        ),
        migrations.AlterField(
            model_name='contents_categories',
            name='category_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 20, 50, 2, 938324)),
        ),
    ]