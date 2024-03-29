# Generated by Django 4.1.4 on 2022-12-30 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newz_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_is_active', models.BooleanField(default=True)),
                ('category_publish_in', models.DateTimeField(default=datetime.datetime(2022, 12, 30, 9, 0, 16, 910892))),
            ],
        ),
        migrations.CreateModel(
            name='newz_article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=200)),
                ('article_content', models.TextField()),
                ('article_is_active', models.BooleanField(default=True)),
                ('article_publish_in', models.DateTimeField(default=datetime.datetime(2022, 12, 30, 9, 0, 16, 910892))),
                ('article_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newz.newz_category')),
            ],
        ),
    ]
