# Generated by Django 4.1.4 on 2023-01-31 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scool_brogram', '0008_alter_brogram_lessons_lesson_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brogram_lessons',
            name='lesson_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 3, 32, 35, 906646)),
        ),
        migrations.AlterField(
            model_name='brogram_times',
            name='time_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 3, 32, 35, 906646)),
        ),
    ]