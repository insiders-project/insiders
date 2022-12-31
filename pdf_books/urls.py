from django.urls import path
from . import views

urlpatterns =[
    path("",views.pdf_books_stages,name="pdf_books_stages"),
    path("stages/<int:pk>",views.pdf_books_classes,name="pdf_books_classes"),
    path("classes/<int:pk>",views.pdf_books_study_terms,name="pdf_books_study_terms"),
    path("study-terms/<int:pk>",views.pdf_books_books,name="pdf_books_books"),
    path("books/<int:pk>",views.pdf_books_book,name="pdf_books_book")
]