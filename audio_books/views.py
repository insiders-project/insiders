from django.shortcuts import render
from.models import Audio_books_stages, Audio_books_classes, Audio_books_study_terms, Audio_books_books, Audio_books_units, Audio_books_lessons
from .models import Audio_books_stages, Audio_books_classes, Audio_books_study_terms, Audio_books_books, Audio_books_units, Audio_books_lessons

# Create your views here.

def audio_books_stages(request):
    stages = Audio_books_stages.objects.all()
    return render(request, "audio_books/stages.html", {"stages": stages})


def audio_books_classes(request, pk):
    stage = Audio_books_stages.objects.get(pk=pk)
    classes = Audio_books_classes.objects.filter(class_stage=stage)
    return render(request, "audio_books/classes.html", {
        "stage": stage,
        "classes": classes
    })


def audio_books_study_terms(request, pk):
    Class = Audio_books_classes.objects.get(pk=pk)
    study_terms = Audio_books_study_terms.objects.filter(study_term_class=Class)
    return render(request, "audio_books/study_terms.html", {
        "Class": Class,
        "study_terms": study_terms,
    })
def audio_books_books(request, pk):
        study_term = Audio_books_study_terms.objects.get(pk=pk)
        books = Audio_books_books.objects.filter(book_study_term=study_term)
        return render(request, "audio_books/books.html", {
            "study_term": study_term,
            "books": books,
        })

def audio_books_units (request,pk):
    book =Audio_books_books.objects.get(pk=pk)
    units =Audio_books_units.objects.filter(unit_book=book)
    return render(request,"audio_books/units.html",{
        "book":book,
        "units":units
    })

def audio_books_lessons(request,pk):
    unit =Audio_books_units.objects.get(pk=pk)
    lessons =Audio_books_lessons.objects.filter(lesson_unit=unit)
    return render(request,"audio_books/lessons.html",{
        "unit":unit,
        "lessons":lessons,
    })
def audio_books_lesson(request, pk):
    lesson = Audio_books_lessons.objects.get(pk=pk)
    return render(request, "audio_books/lesson.html", {
        "lesson": lesson,
    })
