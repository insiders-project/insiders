from django.db import models
from django.contrib.auth.models import User
from scool.models import *
import datetime

media_types =[
    ("docx","docx"),
    ("pdf","pdf"),
    ("audio","audio"),
    ("vidio","vidio"),
]
# Create your models here.

class Lessons_urls (models.Model):
    url_name =models.CharField(max_length=250)
    url_type =models.CharField(max_length=10,choices=media_types)
    url_stage =models.ForeignKey(School_stages,on_delete=models.CASCADE)
    url_class =models.ForeignKey(School_classes,on_delete=models.CASCADE)
    url_study_term =models.ForeignKey(School_study_terms,on_delete=models.CASCADE)
    url_subject =models.ForeignKey(School_subjects,on_delete=models.CASCADE)
    url_unit =models.ForeignKey(School_units,on_delete=models.CASCADE)
    url_lesson=models.ForeignKey(School_lessons,on_delete=models.CASCADE)
    url =models.URLField()
    url_is_active =models.BooleanField(default=True)
    url_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    url_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.url_name


class Lessons_files (models.Model):
    file_name =models.CharField(max_length=250)
    file_type =models.CharField(max_length=10,choices=media_types)
    file_stage =models.ForeignKey(School_stages,on_delete=models.CASCADE)
    file_class =models.ForeignKey(School_classes,on_delete=models.CASCADE)
    file_study_term =models.ForeignKey(School_study_terms,on_delete=models.CASCADE)
    file_subject =models.ForeignKey(School_subjects,on_delete=models.CASCADE)
    file_unit =models.ForeignKey(School_units,on_delete=models.CASCADE)
    file_lesson=models.ForeignKey(School_lessons,on_delete=models.CASCADE)
    file =models.FileField(upload_to="files/")
    file_is_active =models.BooleanField(default=True)
    file_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    file_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.file_name
