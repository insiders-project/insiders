from django.urls import path
from . import views
urlpatterns =[
    path("",views.serch,name="serch"),
    path("books",views.rezolts,name="books"),
]