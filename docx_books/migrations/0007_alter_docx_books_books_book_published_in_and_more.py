# Generated by Django 4.1.4 on 2022-12-30 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docx_books', '0006_alter_docx_books_books_book_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docx_books_books',
            name='book_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 8, 6, 30, 120335)),
        ),
        migrations.AlterField(
            model_name='docx_books_classes',
            name='class_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 8, 6, 30, 120335)),
        ),
        migrations.AlterField(
            model_name='docx_books_stages',
            name='stage_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 8, 6, 30, 51319)),
        ),
        migrations.AlterField(
            model_name='docx_books_study_terms',
            name='study_term_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 8, 6, 30, 120335)),
        ),
    ]
