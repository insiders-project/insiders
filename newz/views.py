from django.shortcuts import render
from .models import Newz_categories, Newz_articles

# Create your views here.

def newz_articles(request):
    articles =Newz_articles.objects.all()
    return render(request,"newz/articles.html",{
        "articles":articles
    })

def newz_article(request,pk):
    article =Newz_articles.objects.get(pk=pk)
    return render(request,"newz/article.html",{
    "article":article,
})