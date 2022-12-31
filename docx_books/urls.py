from django.urls import path
from . import views

urlpatterns =[
    path("",views.docx_books_stages,name="docx_books_stages"),
    path("stages/<int:pk>",views.docx_books_classes,name="docx_books_classes"),
    path("classes/<int:pk>",views.docx_books_study_terms,name="docx_books_study_terms"),
    path("study-terms/<int:pk>",views.docx_books_books,name="docx_books_books"),
    path("books/<int:pk>",views.docx_books_book,name="docx_books_book")
]