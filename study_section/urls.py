from django.urls import path
from . import views

urlpatterns =[
path ("",views.stages,name="study_stages"),
path ("stages/<int:pk>",views.classes,name="study_classes"),
path("add-class/<int:pk>",views.add_class,name="add_class"),
path ("classes/<int:pk>",views.study_terms,name="study_study_terms"),
path("add-study-term/<int:pk>",views.add_study_term,name="add_study_term"),
path ("study_terms/<int:pk>",views.subjects,name="study_subjects"),
path ("add-subject/<int:pk>",views.add_subject,name="add_subject"),
path ("subjects/<int:pk>", views.units,name="study_units"),
path ("add-unit/<int:pk>",views.add_unit,name="add_unit"),
path ("units/<int:pk>",views.lessons,name="study_lessons"),
path("add-lesson/<int:pk>",views.add_lesson,name="add_lesson"),
path ("lesons/<int:pk>",views.lesson,name="study_lesson"),
]