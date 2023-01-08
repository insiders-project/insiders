from django.db import models
import datetime

# Create your models here.

class Posts (models.Model):
    post_title =models.CharField()
    post_content =models.TextField()
    post_is_active =models.BooleanField(default=True)
    post_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__ (self):
        return self.post_title

class Posts_comments (models.Model):
    comment_for =models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment_content =models.TextField()
    comment_is_active =models.BooleanField(default=True)
    comment_published_in =models.DateTimeField(default=datetime.datetime.now())

    def __str__ (self):
        return self.comment_content

class Comments_replies (models.Model):
    reply_for =models.ForeignKey(Posts_comments,on_delete=models.CASCADE)