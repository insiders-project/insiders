from django.db import models
from django.contrib.auth.models import User 
import datetime
# Create your models here.

class Scool_stages (models.Model):
    stage_name = models.CharField(max_length=50)
    stage_is_active = models.BooleanField(default=True)
    stage_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    stage_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.stage_name

class Scool_classes(models.Model):
    class_name = models.CharField(max_length=50)
    class_stage = models.ForeignKey(Scool_stages, on_delete=models.CASCADE)
    class_is_active = models.BooleanField(default=True)
    class_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    class_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.class_name


class Scool_sections (models.Model):
    section_name =models.CharField(max_length=50)
    section_stage =models.ForeignKey(Scool_stages,on_delete=models.CASCADE)
    section_class =models.ForeignKey(Scool_classes,on_delete=models.CASCADE)
    section_is_active = models.BooleanField(default=True)
    section_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    section_published_in = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return self.class_name

class Brogram_times (models.Model):
    time_name =models.CharField(max_length=50)
    time_start_from =models.TimeField()
    time_end_in =models.TimeField()

class Brogram_lessons (models.Model):
    lesson_stage =models.ForeignKey(Scool_stages,on_delete=models.CASCADE)
    lesson_class =models.ForeignKey(Scool_classes,on_delete=models.CASCADE)
    lesson_class =models.ForeignKey(Scool_classes,on_delete=models.CASCADE)