from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class School_stages (models.Model):
    stage_name = models.CharField(max_length=50)
    stage_is_active = models.BooleanField(default=True)
    stage_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    stage_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.stage_name
    
    class Meta:
        verbose_name ="مرحلة دراسية"
        verbose_name_plural ="المراحل الدراسية"

class School_classes(models.Model):
    class_name = models.CharField(max_length=50)
    class_stage = models.ForeignKey(School_stages, on_delete=models.CASCADE)
    class_is_active = models.BooleanField(default=True)
    class_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    class_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name ="صف دراسي"
        verbose_name_plural ="الصفوف الدراسية"



class School_sections (models.Model):
    section_name =models.CharField(max_length=50)
    section_stage =models.ForeignKey(School_stages,on_delete=models.CASCADE)
    section_class =models.ForeignKey(School_classes,on_delete=models.CASCADE)
    section_is_active = models.BooleanField(default=True)
    section_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    section_published_in = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name ="شعبة"
        verbose_name_plural ="الشعب"



class School_study_terms(models.Model):
    study_term_name = models.CharField(max_length=50)
    study_term_stage =models.ForeignKey(School_stages,on_delete=models.CASCADE)
    study_term_class =models.ForeignKey(School_classes,on_delete=models.CASCADE)
    study_term_is_active = models.BooleanField(default=True)
    study_term_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    study_term_published_in = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.study_term_name

    class Meta:
        verbose_name ="فصل دراسي"
        verbose_name_plural ="الفصول الدراسية"


class School_subjects(models.Model):
    subject_name =models.CharField(max_length=50)
    subject_stage =models.ForeignKey(School_stages,on_delete=models.CASCADE)
    subject_class =models.ForeignKey(School_classes,on_delete=models.CASCADE)
    subject_study_term =models.ForeignKey(School_study_terms,on_delete=models.CASCADE)
    subject_is_active = models.BooleanField(default=True)
    subject_created_by =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)    
    subject_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.subject_name
    class Meta:
        verbose_name ="مادة"
        verbose_name_plural ="المواد"


class School_units (models.Model):
    unit_name =models.CharField(max_length=50)
    unit_stage =models.ForeignKey(School_stages,on_delete=models.CASCADE)
    unit_class =models.ForeignKey(School_classes,on_delete=models.CASCADE)
    unit_study_term =models.ForeignKey(School_study_terms,on_delete=models.CASCADE)
    unit_subject =models.ForeignKey(School_subjects,on_delete=models.CASCADE)
    unit_is_active = models.BooleanField(default=True)
    unit_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    unit_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.unit_name

    class Meta:
        verbose_name ="وحدة دراسية"
        verbose_name_plural ="الوحدات الدراسية"


class School_lessons (models.Model):
    lesson_name =models.CharField(max_length=50)
    lesson_stage =models.ForeignKey(School_stages,on_delete=models.CASCADE)
    lesson_class =models.ForeignKey(School_classes,on_delete=models.CASCADE)
    lesson_study_term =models.ForeignKey(School_study_terms,on_delete=models.CASCADE)
    lesson_subject =models.ForeignKey(School_subjects,on_delete=models.CASCADE)
    lesson_unit =models.ForeignKey(School_units,on_delete=models.CASCADE)
    lesson_is_active = models.BooleanField(default=True)
    lesson_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    lesson_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.lesson_name

    class Meta:
        verbose_name ="درس"
        verbose_name_plural ="الدروس"
