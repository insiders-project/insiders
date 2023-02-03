from django.urls import path
from . import views

urlpatterns =[
    path ("",views.stages,name="scool_brogram_stages"),
    path ("stages/<int:pk>",views.classes,name="scool_brogram_classes"),
    path ("classes/<int:pk>",views.sections,name="scool_brogram_sections"),
    path ("section/<int:pk>",views.lessons,name="scool_brogram_lessons"),
    
]