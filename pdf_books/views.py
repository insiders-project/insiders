from django.shortcuts import render
from .models import Pdf_books_stages, Pdf_books_classes, Pdf_books_study_terms, Pdf_books_books

# Create your views here.


def pdf_books_stages(request):
    stages = Pdf_books_stages.objects.all()
    return render(request, "pdf_books/stages.html", {"stages": stages})


def pdf_books_classes(request, pk):
    stage = Pdf_books_stages.objects.get(pk=pk)
    classes = Pdf_books_classes.objects.filter(class_stage=stage)
    return render(request, "pdf_books/classes.html", {
        "stage": stage,
        "classes": classes
    })


def pdf_books_study_terms(request, pk):
    Class = Pdf_books_classes.objects.get(pk=pk)
    study_terms = Pdf_books_study_terms.objects.filter(study_term_class=Class)
    return render(request, "pdf_books/study_terms.html", {
        "Class": Class,
        "study_terms": study_terms,
    })
def pdf_books_books(request, pk):
        study_term = Pdf_books_study_terms.objects.get(pk=pk)
        books = Pdf_books_books.objects.filter(book_study_term=study_term)
        return render(request, "pdf_books/books.html", {
            "study_term": study_term,
            "books": books,
        })


def pdf_books_book(request, pk):
    book = Pdf_books_books.objects.get(pk=pk)
    return render(request, "pdf_books/book.html", {
        "book": book,
    })
