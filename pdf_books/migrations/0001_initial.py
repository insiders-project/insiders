# Generated by Django 4.1 on 2022-09-19 08:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdf_books_classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('class_is_active', models.BooleanField(default=True)),
                ('class_published_in', models.DateTimeField(default=datetime.datetime(2022, 9, 19, 11, 25, 23, 870931))),
            ],
        ),
        migrations.CreateModel(
            name='pdf_books_stages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=50)),
                ('stage_is_active', models.BooleanField(default=True)),
                ('stage_published_in', models.DateTimeField(default=datetime.datetime(2022, 9, 19, 11, 25, 23, 870931))),
            ],
        ),
        migrations.CreateModel(
            name='pdf_books_study_terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_term_name', models.CharField(max_length=50)),
                ('study_term_is_active', models.BooleanField(default=True)),
                ('study_term_published_in', models.DateTimeField(default=datetime.datetime(2022, 9, 19, 11, 25, 23, 870931))),
                ('study_term_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf_books.pdf_books_classes')),
                ('study_term_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf_books.pdf_books_stages')),
            ],
        ),
        migrations.AddField(
            model_name='pdf_books_classes',
            name='class_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf_books.pdf_books_stages'),
        ),
        migrations.CreateModel(
            name='pdf_books_books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_is_active', models.BooleanField(default=True)),
                ('book_published_in', models.DateTimeField(default=datetime.datetime(2022, 9, 19, 11, 25, 23, 870931))),
                ('book_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf_books.pdf_books_classes')),
                ('book_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf_books.pdf_books_stages')),
                ('book_study_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdf_books.pdf_books_study_terms')),
            ],
        ),
    ]