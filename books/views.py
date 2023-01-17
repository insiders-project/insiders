from django.shortcuts import render
from .models import Books_stages, Books_classes, Books_study_terms, Books, Books_files, Books_urls

# Create your views here.

def serch(request):
    stages =Books_stages.objects.all()
    classes =Books_classes.objects.all()
    study_terms =Books_study_terms.objects.all()
    return render(request,"books/serch.html",{
        "stages":stages,
        "classes":classes,
        "study_terms":study_terms,
    })

def rezolts (request):
    get_stage =None
    get_class =None
    get_study_term =None
    if request.method=="GET":
        if "stage" in request.GET:
            get_stage =request.GET.get("stage")
        if "class" in request.GET:
            get_class =request.GET.get("class")
        if "study_term"in request.GET:
            get_study_term =request.GET.get("study_term")
            rezolt =Books.objects.all().filter(book_stage=get_stage,book_class=get_class,book_study_term=get_study_term)
        return render(request,"books/books.html",{
            "books":rezolt
        })
    else :
        return render(request,"alerts/obs.html")


