from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Forums (models.Model):
    forum_name =models.CharField(max_length=25)
    forum_description =models.TextField()
    forum_is_active = models.BooleanField(default=True)
    forum_created_by =models.ForeignKey(User,on_delete=models.CASCADE)    
    forum_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.forum_name

class Forums_posts (models.Model):
    post_name =models.CharField(max_length=250)
    post_forum =models.ForeignKey(Forums,on_delete=models.CASCADE)
    post_content =models.TextField()
    post_is_active = models.BooleanField(default=True)
    post_created_by =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)    
    posted_by =models.CharField(max_length=50)
    post_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.post_name


class Forums_comments (models.Model):
    comment_forum =models.ForeignKey(Forums,on_delete=models.CASCADE)
    comment_post =models.ForeignKey(Forums_posts,on_delete=models.CASCADE)
    comment_content =models.TextField()
    comment_is_active = models.BooleanField(default=True)
    comment_created_by =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)    
    commented_by =models.CharField(max_length=50)
    comment_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.comment_content

class Forums_replies (models.Model):
    reply_forum =models.ForeignKey(Forums,on_delete=models.CASCADE)
    reply_post =models.ForeignKey(Forums_posts,on_delete=models.CASCADE)
    reply_comment =models.ForeignKey(Forums_comments,on_delete=models.CASCADE)
    reply_content =models.TextField()
    reply_is_active = models.BooleanField(default=True)
    reply_created_by =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)    
    replyed_by =models.CharField(max_length=50)
    reply_published_in = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.reply_content
