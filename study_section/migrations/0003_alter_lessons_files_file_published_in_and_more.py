# Generated by Django 4.1.4 on 2023-01-24 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_section', '0002_alter_lessons_files_file_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons_files',
            name='file_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 16, 55, 16, 104374)),
        ),
        migrations.AlterField(
            model_name='lessons_urls',
            name='url_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 16, 55, 16, 88750)),
        ),
    ]