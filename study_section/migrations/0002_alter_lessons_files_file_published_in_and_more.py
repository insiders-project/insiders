# Generated by Django 4.1.4 on 2023-01-21 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_section', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons_files',
            name='file_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 2, 0, 42, 36421)),
        ),
        migrations.AlterField(
            model_name='lessons_urls',
            name='url_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 2, 0, 42, 36421)),
        ),
    ]
