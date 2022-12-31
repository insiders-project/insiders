from django.shortcuts import render
from .models import Docx_books_stages, Docx_books_classes, Docx_books_study_terms, Docx_books_books

# Create your views here.


def docx_books_stages(request):
    stages = Docx_books_stages.objects.all()
    return render(request, "docx_books/stages.html", {"stages": stages})


def docx_books_classes(request, pk):
    stage = Docx_books_stages.objects.get(pk=pk)
    classes = Docx_books_classes.objects.filter(class_stage=stage)
    return render(request, "docx_books/classes.html", {
        "stage": stage,
        "classes": classes
    })


def docx_books_study_terms(request, pk):
    Class = Docx_books_classes.objects.get(pk=pk)
    study_terms = Docx_books_study_terms.objects.filter(study_term_class=Class)
    return render(request, "docx_books/study_terms.html", {
        "Class": Class,
        "study_terms": study_terms,
    })
def docx_books_books(request, pk):
        study_term = Docx_books_study_terms.objects.get(pk=pk)
        books = Docx_books_books.objects.filter(book_study_term=study_term)
        return render(request, "docx_books/books.html", {
            "study_term": study_term,
            "books": books,
        })


def docx_books_book(request, pk):
    book = Docx_books_books.objects.get(pk=pk)
    return render(request, "docx_books/book.html", {
        "book": book,
    })
