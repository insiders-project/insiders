from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Forums (models.Model):
    forum_name =models.CharField(max_length=25)
    forum_description =models.TextField()