from django.db import models
import datetime

# Create your models here.

class Contents_categories (models.Model):
    category_name =models.CharField(max_length=50)
    category_is_active =models.BooleanField(default=True)
    category_publish_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.category_name

class Contents(models.Model):
    content_name =models.CharField(max_length=200)
    content_desscription =models.TextField()
    content_category =models.ForeignKey(Contents_categories,on_delete=models.CASCADE)
    content_url =models.URLField()
    content_is_active =models.BooleanField(default=True)
    content_publish_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.content_name