from django.shortcuts import render
from scool.models import *
from .models import *

# Create your views here.

def stages (request):
    stages =School_stages.objects.filter(stage_is_active=True)
    return render(request,"study_section/stages.html",{
        "stages":stages,
    })

def add_class(request,pk):
    name =None
    stage =School_stages.objects.get(pk=pk)
    is_active =None
    created_by =request.user
    if request.method == "POST":
        if "name" in request.POST:
            name =request.POST ["name"]
        if "is_active" in request.POST:
            is_active =request.POST["is_active"]
        add_class =School_classes(class_name=name,class_stage=stage,class_is_active=is_active,class_created_by=created_by)
        add_class.save()
    return render(request,"study_section/add_class.html")

def add_study_term(request,pk):
    name =None
    Class =School_classes.objects.get(pk=pk)
    stage =Class.class_stage
    is_active =None
    created_by =request.user
    if request.method == "POST":
        if "name" in request.POST:
            name =request.POST ["name"]
        if "is_active" in request.POST:
            is_active =request.POST["is_active"]
        add_study_term =School_study_terms(study_term_name=name,study_term_stage=stage,study_term_class=Class,study_term_is_active=is_active,study_term_created_by=created_by)
        add_study_term.save()
    return render(request,"study_section/add_study_term.html")

def add_subject(request,pk):
    name =None
    study_term =School_study_terms.objects.get(pk=pk)
    stage =study_term.study_term_stage
    Class =study_term.study_term_class
    is_active =None
    created_by =request.user
    if request.method == "POST":
        if "name" in request.POST:
            name =request.POST ["name"]
        if "is_active" in request.POST:
            is_active =request.POST["is_active"]
        add_subject =School_subjects(subject_name=name,subject_stage=stage,subject_class=Class,subject_study_term=study_term,subject_is_active=is_active,subject_created_by=created_by)
        add_subject.save()
    return render(request,"study_section/add_subject.html",{
        "study_term":study_term,
    })

def add_unit (request,pk):
    name =None
    subject =School_subjects.objects.get(pk=pk)
    stage =subject.subject_stage
    Class =subject.subject_class
    study_term =subject.subject_study_term
    is_active =None
    created_by =request.user
    if request.method == "POST":
        if "name" in request.POST:
            name =request.POST ["name"]
        if "is_active" in request.POST:
            is_active =request.POST ["is_active"]
        add_unit =School_units(unit_name=name,unit_stage=stage,unit_class=Class,unit_study_term=study_term,unit_subject=subject,unit_is_active=is_active,unit_created_by=created_by)
        add_unit.save()
    return render (request,"study_section/add_unit.html")

def add_lesson (request,pk):
    name =None
    unit =School_units.objects.get(pk=pk)
    stage =unit.unit_stage
    Class =unit.unit_class
    study_term =unit.unit_study_term
    subject =unit.unit_subject
    is_active =None
    created_by =request.user
    if request.method == "POST":
        if "name" in request.POST:
            name =request.POST ["name"]
        if "is_active" in request.POST:
            is_active =request.POST ["is_active"]
        add_lesson =School_lessons(lesson_name=name,lesson_stage=stage,lesson_class=Class,lesson_study_term=study_term,lesson_subject=subject,lesson_unit=unit,lesson_is_active=is_active,lesson_created_by=created_by)
        add_lesson.save()
    return render (request,"study_section/add_lesson.html")


def classes (request,pk):
    stage =School_stages.objects.get(pk=pk)
    classes =School_classes.objects.filter(class_stage=stage,class_is_active=True)
    return render(request,"study_section/classes.html",{
        "classes":classes,
    })

def study_terms (request,pk):
    Class =School_classes.objects.get(pk=pk)
    study_terms =School_study_terms.objects.filter(study_term_class=Class,study_term_is_active=True)
    return render(request,"study_section/study_terms.html",{
        "study_terms":study_terms
    })

def subjects (request,pk):
    study_term =School_study_terms.objects.get(pk=pk)
    subjects =School_subjects.objects.filter(subject_study_term=study_term,subject_is_active=True)
    return render(request,"study_section/subjects.html",{
        "subjects":subjects,
    })

def units (request,pk):
    subject =School_subjects.objects.get(pk=pk)
    units =School_units.objects.filter(unit_subject=subject,unit_is_active=True)
    return render (request,"study_section/units.html",{
        "units":units
    })

def lessons (request,pk):
    unit =School_units.objects.get(pk=pk)
    lessons =School_lessons.objects.filter(lesson_unit=unit,lesson_is_active=True)
    return render (request,"study_section/lessons.html",{
        "lessons":lessons
    })


def lesson (request,pk):
    lesson =School_lessons.objects.get(pk=pk)
    docx_urls =Lessons_urls.objects.filter(url_type="docx",url_lesson=lesson,url_is_active=True)
    pdf_urls =Lessons_urls.objects.filter(url_type="pdf",url_lesson=lesson,url_is_active=True)
    audio_urls =Lessons_urls.objects.filter(url_type="audio",url_lesson=lesson,url_is_active=True)
    vidio_urls =Lessons_urls.objects.filter(url_type="vidio",url_lesson=lesson,url_is_active=True)
    docx_files =Lessons_files.objects.filter(file_type="docx",file_lesson=lesson,file_is_active=True)
    pdf_files =Lessons_files.objects.filter(file_type="pdf",file_lesson=lesson,file_is_active=True)
    audio_files =Lessons_files.objects.filter(file_type="audio",file_lesson=lesson,file_is_active=True)
    vidio_files =Lessons_files.objects.filter(file_type="vidio",file_lesson=lesson,file_is_active=True)
    return render(request,"study_section/lesson.html",{
        "lesson":lesson,
        "docx_urls":docx_urls,
        "pdf_urls":pdf_urls,
        "audio_urls":audio_urls,
        "vidio_urls":vidio_urls,
        "docx_files":docx_files,
        "pdf_files":pdf_files,
        "audio_files":audio_files,
        "vidio_files":vidio_files,
    })