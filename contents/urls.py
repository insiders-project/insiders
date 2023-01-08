from django.urls import path
from . import views

urlpatterns =[
    path("",views.contents_categories,name="contents_categories"),
    path("categories<int:pk>",views.contents,name="contents"),
    path("contents<int:pk>",views.content,name="content"),
]