from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Audio_books_stages)
admin.site.register(models.Audio_books_classes)
admin.site.register(models.Audio_books_study_terms)
admin.site.register(models.Audio_books_books)
admin.site.register(models.Audio_books_units)
admin.site.register(models.Audio_books_lessons)