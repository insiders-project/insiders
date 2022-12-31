# Generated by Django 4.1.4 on 2022-12-30 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf_books', '0008_alter_pdf_books_books_book_published_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf_books_books',
            name='book_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 10, 0, 38, 118981)),
        ),
        migrations.AlterField(
            model_name='pdf_books_classes',
            name='class_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 10, 0, 38, 118981)),
        ),
        migrations.AlterField(
            model_name='pdf_books_stages',
            name='stage_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 10, 0, 38, 118981)),
        ),
        migrations.AlterField(
            model_name='pdf_books_study_terms',
            name='study_term_published_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 30, 10, 0, 38, 118981)),
        ),
    ]
