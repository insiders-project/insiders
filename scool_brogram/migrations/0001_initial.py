# Generated by Django 4.1.4 on 2023-01-21 17:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scool', '0011_alter_scool_classes_class_published_in_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brogram_days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=50)),
                ('day_is_active', models.BooleanField(default=True)),
                ('day_published_in', models.DateTimeField(default=datetime.datetime(2023, 1, 21, 20, 32, 34, 875326))),
                ('day_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Brogram_times',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_name', models.CharField(max_length=50)),
                ('time_start_from', models.TimeField()),
                ('time_end_in', models.TimeField()),
                ('time_is_active', models.BooleanField(default=True)),
                ('time_published_in', models.DateTimeField(default=datetime.datetime(2023, 1, 21, 20, 32, 34, 875326))),
                ('time_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Brogram_lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leson_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scool.scool_subjects')),
                ('lesson_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scool.scool_classes')),
                ('lesson_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scool_brogram.brogram_days')),
                ('lesson_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scool.scool_sections')),
                ('lesson_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scool.scool_stages')),
                ('lesson_study_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scool.scool_study_terms')),
                ('lesson_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scool_brogram.brogram_times')),
            ],
        ),
    ]