from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Docx_books_stages)
admin.site.register(models.Docx_books_classes)
admin.site.register(models.Docx_books_study_terms)
admin.site.register(models.Docx_books_books)