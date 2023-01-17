from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Books_stages(models.Model):
    stage_name = models.CharField(max_length=50)
    stage_is_active = models.BooleanField(default=True)
    stage_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    stage_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.stage_name

class Books_classes(models.Model):
    class_name = models.CharField(max_length=50)
    class_stage = models.ForeignKey(Books_stages, on_delete=models.CASCADE)
    class_is_active = models.BooleanField(default=True)
    class_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    class_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.class_name

class Books_study_terms(models.Model):
    study_term_name = models.CharField(max_length=50)
    study_term_stage = models.ForeignKey(Books_stages, on_delete=models.CASCADE)
    study_term_class = models.ForeignKey(Books_classes, on_delete=models.CASCADE)
    study_term_is_active = models.BooleanField(default=True)
    study_term_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    study_term_published_in = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.study_term_name

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_stage = models.ForeignKey(Books_stages, on_delete=models.CASCADE)
    book_class = models.ForeignKey(Books_classes, on_delete=models.CASCADE)
    book_study_term = models.ForeignKey(Books_study_terms, on_delete=models.CASCADE)
    book_is_active =models.BooleanField(default=True)
    book_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    book_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.book_name

class Books_files (models.Model):
    types =(
        ("docx","docx"),
        ("pdf","pdf"),
        )
    book_file_name =models.CharField(max_length=50)
    book_file_type =models.CharField(max_length=10,choices=types)
    book_file_stage =models.ForeignKey(Books_stages,on_delete=models.CASCADE)
    book_file_class = models.ForeignKey(Books_classes, on_delete=models.CASCADE)
    book_file_study_term = models.ForeignKey(Books_study_terms, on_delete=models.CASCADE)
    book_file_book =models.ForeignKey(Books,on_delete=models.CASCADE)
    book_file =models.FileField()
    book_file_is_active =models.BooleanField(default=True)
    book_file_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    book_file_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__ (self):
        return self.book_file_name

class Books_urls(models.Model):
    types =(
        ("docx","docx"),
        ("pdf","pdf"),
    )
    book_url_name =models.CharField(max_length=50)
    book_url_type =models.CharField(max_length=10,choices=types)
    book_url_stage =models.ForeignKey(Books_stages,on_delete=models.CASCADE)
    book_url_class = models.ForeignKey(Books_classes, on_delete=models.CASCADE)
    book_url_study_term = models.ForeignKey(Books_study_terms, on_delete=models.CASCADE)
    book_url_book =models.ForeignKey(Books,on_delete=models.CASCADE)
    book_url =models.URLField()
    book_url_is_active =models.BooleanField(default=True)
    book_url_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    book_url_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__ (self):
        return self.book_url_name