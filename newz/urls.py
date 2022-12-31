from django.urls import path
from . import views

urlpatterns =[
    path("",views.newz_articles,name="newz_articles"),
    path("<int:pk>",views.newz_article,name="newz_article"),
]