from django.db import models
from django.contrib.auth.models import User 
from scool.models import *
import datetime
# Create your models here.
days =[
    ("الأحد","الأحد"),
    ("الإثنين","الإثنين"),
    ("الثلاثاء","الثلاثاء"),
    ("الأربعاء","الأربعاء"),
    ("الخميس","الخميس"),
]

class Brogram_times (models.Model):
    time_name =models.CharField(max_length=50)
    time_start_from =models.TimeField()
    time_end_in =models.TimeField()
    time_is_active =models.BooleanField(default=True)
    time_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    time_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.time_name



class Brogram_lessons (models.Model):
    lesson_stage =models.ForeignKey(School_stages,on_delete=models.CASCADE)
    lesson_class =models.ForeignKey(School_classes,on_delete=models.CASCADE)
    lesson_section =models.ForeignKey(School_sections,on_delete=models.CASCADE)
    lesson_study_term =models.ForeignKey(School_study_terms,on_delete=models.CASCADE)
    lesson_subject =models.ForeignKey(School_subjects,on_delete=models.CASCADE)
    lesson_day =models.CharField(max_length=20,choices=days)
    lesson_time =models.ForeignKey(Brogram_times,on_delete=models.CASCADE)
    lesson_is_active = models.BooleanField(default=True)
    lesson_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    lesson_published_in = models.DateTimeField(default=datetime.datetime.now())

