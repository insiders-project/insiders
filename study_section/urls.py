from django.urls import path
from . import views

urlpatterns =[
path ("",views.stages,name="study_stages"),
path ("stages/<int:pk>",views.classes,name="study_classes"),
path ("classes/<int:pk>",views.study_terms,name="study_study_terms"),
path ("study_terms/<int:pk>",views.subjects,name="study_subjects"),
path ("subjects/<int:pk>", views.units,name="study_units"),
path ("units/<int:pk>",views.lessons,name="study_lessons"),
path ("lesons/<int:pk>",views.lesson,name="study_lesson"),
]