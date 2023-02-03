from django.shortcuts import render
from scool.models import *
from .models import *

# Create your views here.

def stages (request):
    stages =Scool_stages.objects.filter(stage_is_active=True)
    return render(request,"study_section/stages.html",{
        "stages":stages,
    })

def classes (request,pk):
    stage =Scool_stages.objects.get(pk=pk)
    classes =Scool_classes.objects.filter(class_stage=stage,class_is_active=True)
    return render(request,"study_section/classes.html",{
        "classes":classes,
    })

def study_terms (request,pk):
    Class =Scool_classes.objects.get(pk=pk)
    study_terms =Scool_study_terms.objects.filter(study_term_class=Class,study_term_is_active=True)
    return render(request,"study_section/study_terms.html",{
        "study_terms":study_terms
    })

def subjects (request,pk):
    study_term =Scool_study_terms.objects.get(pk=pk)
    subjects =Scool_subjects.objects.filter(subject_study_term=study_term,subject_is_active=True)
    return render(request,"study_section/subjects.html",{
        "subjects":subjects,
    })

def units (request,pk):
    subject =Scool_subjects.objects.get(pk=pk)
    units =Scool_units.objects.filter(unit_subject=subject,unit_is_active=True)
    return render (request,"study_section/units.html",{
        "units":units
    })

def lessons (request,pk):
    unit =Scool_units.objects.get(pk=pk)
    lessons =Scool_lessons.objects.filter(lesson_unit=unit,lesson_is_active=True)
    return render (request,"study_section/lessons.html",{
        "lessons":lessons
    })


def lesson (request,pk):
    lesson =Scool_lessons.objects.get(pk=pk)
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