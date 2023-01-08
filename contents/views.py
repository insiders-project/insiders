from django.shortcuts import render
from .models import Contents_categories, Contents

# Create your views here.

def contents_categories (request):
    categories =Contents_categories.objects.all()
    return render(request,"contents/categories.html",{
        "categories":categories,
    })

def contents(request,pk):
    category =Contents_categories.objects.get(pk=pk)
    contents =Contents.objects.filter(content_category=category)
    return render(request,"contents/contents.html",{
        "category":category,
        "contents":contents
    })

def content(request,pk): 
        content =Contents.objects.get(pk=pk) 
        return render(request ,"contents/content.html",{
            "content",content
        })