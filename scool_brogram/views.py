from django.shortcuts import render
from scool.models import *
from .models import *

# Create your views here.
def stages (request):
    stages =School_stages.objects.filter(stage_is_active=True)
    name = None
    is_active = None
    created_by = request.user
    if request.method == "POST":
        if "name" in request.POST:
            name = request.POST["name"]
        if "is_active" in request.POST:
            is_active = request.POST["is_active"]
        add_stage = School_stages(stage_name=name, stage_is_active=is_active, stage_created_by=created_by)
        add_stage.save()

    return render(request,"scool_brogram/stages.html",{
        "stages":stages,
    })

def classes (request,pk):
    stage =School_stages.objects.get(pk=pk)
    classes =School_classes.objects.filter(class_stage=stage,class_is_active=True)

    stage = School_stages.objects.get(pk=pk)
    classes = School_classes.objects.filter(
        class_stage=stage, class_is_active=True)
    name = None
    is_active = None
    created_by = request.user
    if request.method == "POST":
        if "name" in request.POST:
            name = request.POST["name"]
        if "is_active" in request.POST:
            is_active = request.POST["is_active"]
        add_class = School_classes(class_name=name, class_stage=stage,class_is_active=is_active, class_created_by=created_by)
        add_class.save()
    return render(request,"scool_brogram/classes.html",{
        "classes":classes,
    })

def sections (request,pk):
    Class =School_classes.objects.get(pk=pk)
    sections =School_sections.objects.filter(section_class=Class,section_is_active=True)
    
    name = None
    stage = Class.class_stage
    is_active = None
    created_by = request.user
    if request.method == "POST":
        if "name" in request.POST:
            name = request.POST["name"]
        if "is_active" in request.POST:
            is_active = request.POST["is_active"]
        add_section = School_sections(section_name=name, section_stage=stage,section_class=Class, section_is_active=is_active, section_created_by=created_by)
        add_section.save()
    return render(request,"scool_brogram/sections.html",{
        "sections":sections,
    })

def lessons(request,pk):
    section =School_sections.objects.get(pk=pk)
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