from operator import truediv
from django.db import models
import datetime

# Create your models here.


class Docx_books_stages(models.Model):
    stage_name = models.CharField(max_length=50)
    stage_is_active = models.BooleanField(default=True)
    stage_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.stage_name

class Docx_books_classes(models.Model):
    class_name = models.CharField(max_length=50)
    class_stage = models.ForeignKey(Docx_books_stages, on_delete=models.CASCADE)
    class_is_active = models.BooleanField(default=True)
    class_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.class_name

class Docx_books_study_terms(models.Model):
    study_term_name = models.CharField(max_length=50)
    study_term_stage = models.ForeignKey(Docx_books_stages, on_delete=models.CASCADE)
    study_term_class = models.ForeignKey(Docx_books_classes, on_delete=models.CASCADE)
    study_term_is_active = models.BooleanField(default=True)
    study_term_published_in = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.study_term_name

class Docx_books_books(models.Model):
    book_name = models.CharField(max_length=100)
    book_stage = models.ForeignKey(Docx_books_stages, on_delete=models.CASCADE)
    book_class = models.ForeignKey(Docx_books_classes, on_delete=models.CASCADE)
    book_study_term = models.ForeignKey(Docx_books_study_terms, on_delete=models.CASCADE)
    book_is_active =models.BooleanField(default=True)
    book_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.book_name