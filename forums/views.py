from django.shortcuts import render
from .forms import *

# Create your views here.

def add_forum(request):
    form =Add_post_form()
    if(request.method=="POST"):
        form =Add_post_form(request.POST)
        form.save()
    return render(request,"forums/add_forum.html",{
        "form":form
    })

