from django.db import models
import datetime

# Create your models here.

class Audio_books_stages(models.Model):
    stage_name = models.CharField(max_length=50)
    stage_is_active = models.BooleanField(default=True)
    stage_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.stage_name

class Audio_books_classes(models.Model):
    class_name = models.CharField(max_length=50)
    class_stage = models.ForeignKey(Audio_books_stages, on_delete=models.CASCADE)
    class_is_active = models.BooleanField(default=True)
    class_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.class_name

class Audio_books_study_terms(models.Model):
    study_term_name = models.CharField(max_length=50)
    study_term_stage = models.ForeignKey(Audio_books_stages, on_delete=models.CASCADE)
    study_term_class = models.ForeignKey(Audio_books_classes, on_delete=models.CASCADE)
    study_term_is_active = models.BooleanField(default=True)
    study_term_published_in = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.study_term_name

class Audio_books_books(models.Model):
    book_name = models.CharField(max_length=100)
    book_stage = models.ForeignKey(Audio_books_stages, on_delete=models.CASCADE)
    book_class = models.ForeignKey(Audio_books_classes, on_delete=models.CASCADE)
    book_study_term = models.ForeignKey(Audio_books_study_terms, on_delete=models.CASCADE)
    book_is_active =models.BooleanField(default=True)
    book_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.book_name

class Audio_books_units (models.Model):
    unit_name =models.CharField(max_length=50)
    unit_stage = models.ForeignKey(Audio_books_stages, on_delete=models.CASCADE)
    unit_class = models.ForeignKey(Audio_books_classes, on_delete=models.CASCADE)
    unit_study_term = models.ForeignKey(Audio_books_study_terms, on_delete=models.CASCADE)
    unit_book =models.ForeignKey(Audio_books_books,on_delete=models.CASCADE)
    unit_is_active =models.BooleanField(default=True)
    unit_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__ (self):
        return self.unit_name

class Audio_books_lessons (models.Model):
    lesson_name =models.CharField(max_length=50)
    lesson_stage = models.ForeignKey(Audio_books_stages, on_delete=models.CASCADE)
    lesson_class = models.ForeignKey(Audio_books_classes, on_delete=models.CASCADE)
    lesson_study_term = models.ForeignKey(Audio_books_study_terms, on_delete=models.CASCADE)
    lesson_book =models.ForeignKey(Audio_books_books,on_delete=models.CASCADE)
    lesson_unit =models.ForeignKey(Audio_books_units,on_delete=models.CASCADE)
    lesson_is_active =models.BooleanField(default=True)
    lesson_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__ (self):
        return self.lesson_name
