# Generated by Django 4.1.4 on 2023-01-11 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_books', '0012_alter_pdf_books_books_book_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf_books_books',
            name='book_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 1, 44, 51, 845879)),
        ),
        migrations.AlterField(
            model_name='pdf_books_classes',
            name='class_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 1, 44, 51, 845879)),
        ),
        migrations.AlterField(
            model_name='pdf_books_stages',
            name='stage_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 1, 44, 51, 845879)),
        ),
        migrations.AlterField(
            model_name='pdf_books_study_terms',
            name='study_term_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 1, 44, 51, 845879)),
        ),
    ]
