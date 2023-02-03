from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Newz_categories (models.Model):
    category_name =models.CharField(max_length=50)
    category_is_active =models.BooleanField(default=True)
    category_created_by =models.ForeignKey(User,on_delete=models.CASCADE)
    category_publish_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.category_name

class Newz_articles (models.Model):
    article_name =models.CharField(max_length=200)
    article_category =models.ForeignKey(Newz_categories,on_delete=models.CASCADE)
    article_content =models.TextField()
    article_is_active =models.BooleanField(default=True)
    article_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    article_publish_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.article_name