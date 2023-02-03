from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Forums)
admin.site.register(Forums_posts)
admin.site.register(Forums_comments)
admin.site.register(Forums_replies)