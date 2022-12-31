from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Newz_categories)
admin.site.register(models.Newz_articles)