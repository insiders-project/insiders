# Generated by Django 4.1.4 on 2022-12-30 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_books', '0002_alter_audio_books_books_book_published_in_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audio_books_lessons',
            old_name='lisson_study_term',
            new_name='lesson_study_term',
        ),
        migrations.AlterField(
            model_name='audio_books_books',
            name='book_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 7, 59, 1, 374291)),
        ),
        migrations.AlterField(
            model_name='audio_books_classes',
            name='class_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 7, 59, 1, 374291)),
        ),
        migrations.AlterField(
            model_name='audio_books_lessons',
            name='lesson_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 7, 59, 1, 374291)),
        ),
        migrations.AlterField(
            model_name='audio_books_stages',
            name='stage_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 7, 59, 1, 374291)),
        ),
        migrations.AlterField(
            model_name='audio_books_study_terms',
            name='study_term_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 7, 59, 1, 374291)),
        ),
        migrations.AlterField(
            model_name='audio_books_units',
            name='unit_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 7, 59, 1, 374291)),
        ),
    ]
