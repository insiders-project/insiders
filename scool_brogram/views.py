from django.shortcuts import render
from scool.models import *
from .models import *

# Create your views here.
def stages (request):
    stages =Scool_stages.objects.filter(stage_is_active=True)
    return render(request,"scool_brogram/stages.html",{
        "stages":stages,
    })

def classes (request,pk):
    stage =Scool_stages.objects.get(pk=pk)
    classes =Scool_classes.objects.filter(class_stage=stage,class_is_active=True)
    return render(request,"scool_brogram/classes.html",{
        "classes":classes,
    })

def sections (request,pk):
    Class =Scool_classes.objects.get(pk=pk)
    sections =Scool_sections.objects.filter(section_class=Class,section_is_active=True)
    return render(request,"scool_brogram/sections.html",{
        "sections":sections,
    })

def lessons(request,pk):
    section =Scool_sections.objects.get(pk=pk)
    day_1 =Brogram_lessons.objects.filter(lesson_section=section,lesson_day="الأحد",lesson_is_active=True)
    day_2 =Brogram_lessons.objects.filter(lesson_section=section,lesson_day="الإثنين",lesson_is_active=True)
    day_3 =Brogram_lessons.objects.filter(lesson_section=section,lesson_day="الثلاثاء",lesson_is_active=True)
    day_4 =Brogram_lessons.objects.filter(lesson_section=section,lesson_day="الأربعاء",lesson_is_active=True)
    day_5 =Brogram_lessons.objects.filter(lesson_section=section,lesson_day="الخميس",lesson_is_active=True)
    return render(request,"scool_brogram/lessons.html",{
        "day_1":day_1,
        "day_2":day_2,
        "day_3":day_3,
        "day_4":day_4,
        "day_5":day_5,
    })