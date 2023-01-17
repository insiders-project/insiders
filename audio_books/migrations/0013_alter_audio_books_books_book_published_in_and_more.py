# Generated by Django 4.1.4 on 2023-01-12 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_books', '0012_alter_audio_books_books_book_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_books_books',
            name='book_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 20, 43, 57, 314704)),
        ),
        migrations.AlterField(
            model_name='audio_books_classes',
            name='class_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 20, 43, 57, 314704)),
        ),
        migrations.AlterField(
            model_name='audio_books_lessons',
            name='lesson_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 20, 43, 57, 314704)),
        ),
        migrations.AlterField(
            model_name='audio_books_stages',
            name='stage_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 20, 43, 57, 314704)),
        ),
        migrations.AlterField(
            model_name='audio_books_study_terms',
            name='study_term_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 20, 43, 57, 314704)),
        ),
        migrations.AlterField(
            model_name='audio_books_units',
            name='unit_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 20, 43, 57, 314704)),
        ),
    ]