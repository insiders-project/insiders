# Generated by Django 4.1.4 on 2023-01-07 22:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents_categories',
            name='category_publish_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 8, 1, 8, 47, 283293)),
        ),
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_name', models.CharField(max_length=200)),
                ('content_desscription', models.TextField()),
                ('content_url', models.URLField()),
                ('content_is_active', models.BooleanField(default=True)),
                ('content_publish_in', models.DateTimeField(default=datetime.datetime(2023, 1, 8, 1, 8, 47, 283293))),
                ('content_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.contents_categories')),
            ],
        ),
    ]
