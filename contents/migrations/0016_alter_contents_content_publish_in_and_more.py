# Generated by Django 4.1.4 on 2023-01-20 22:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0015_alter_contents_content_publish_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='content_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 1, 26, 31, 148095)),
        ),
        migrations.AlterField(
            model_name='contents_categories',
            name='category_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 1, 26, 31, 148095)),
        ),
    ]
