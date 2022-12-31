# Generated by Django 4.1.4 on 2022-12-30 06:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_books', '0006_alter_audio_books_books_book_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_books_books',
            name='book_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 9, 0, 16, 895269)),
        ),
        migrations.AlterField(
            model_name='audio_books_classes',
            name='class_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 9, 0, 16, 895269)),
        ),
        migrations.AlterField(
            model_name='audio_books_lessons',
            name='lesson_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 9, 0, 16, 910892)),
        ),
        migrations.AlterField(
            model_name='audio_books_stages',
            name='stage_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 9, 0, 16, 895269)),
        ),
        migrations.AlterField(
            model_name='audio_books_study_terms',
            name='study_term_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 9, 0, 16, 895269)),
        ),
        migrations.AlterField(
            model_name='audio_books_units',
            name='unit_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 9, 0, 16, 910892)),
        ),
    ]
