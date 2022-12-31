from django.urls import path
from . import views

urlpatterns =[
    path("",views.audio_books_stages,name="audio_books_stages"),
    path("stages/<int:pk>",views.audio_books_classes,name="audio_books_classes"),
    path("classes/<int:pk>",views.audio_books_study_terms,name="audio_books_study_terms"),
    path("study-terms/<int:pk>",views.audio_books_books,name="audio_books_books"),
    path("books/<int:pk>",views.audio_books_units,name="audio_books_units"),
    path("units/<int:pk>",views.audio_books_lessons,name="audio_books_lessons"),
    path("lessons/<int:pk>",views.audio_books_lesson,name="audio_books_lesson"),
]