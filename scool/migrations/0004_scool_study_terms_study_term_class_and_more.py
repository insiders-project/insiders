# Generated by Django 4.1.4 on 2023-01-20 17:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scool', '0003_scool_lessons_lesson_study_term_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scool_study_terms',
            name='study_term_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scool.scool_classes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scool_study_terms',
            name='study_term_stage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scool.scool_stages'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scool_classes',
            name='class_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 20, 10, 37, 94296)),
        ),
        migrations.AlterField(
            model_name='scool_lessons',
            name='lesson_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 20, 10, 37, 94296)),
        ),
        migrations.AlterField(
            model_name='scool_sections',
            name='section_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 20, 10, 37, 94296)),
        ),
        migrations.AlterField(
            model_name='scool_stages',
            name='stage_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 20, 10, 37, 94296)),
        ),
        migrations.AlterField(
            model_name='scool_study_terms',
            name='study_term_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 20, 10, 37, 94296)),
        ),
        migrations.AlterField(
            model_name='scool_subjects',
            name='subject_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 20, 10, 37, 94296)),
        ),
        migrations.AlterField(
            model_name='scool_units',
            name='unit_published_in',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 20, 10, 37, 94296)),
        ),
    ]
