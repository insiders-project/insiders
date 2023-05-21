from django.shortcuts import render, redirect, get_object_or_404
from scool.models import *
from .models import *

# Create your views here.


def stages(request):
    stages = School_stages.objects.filter(stage_is_active=True)
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
    return render(request, "study_section/stages.html", {
        "stages": stages,
    })




def classes(request, pk):
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
    return render(request, "study_section/classes.html", {
        "classes": classes,
    })


def study_terms(request, pk):
    Class = School_classes.objects.get(pk=pk)
    study_terms = School_study_terms.objects.filter(study_term_class=Class, study_term_is_active=True)
    name = None
    stage = Class.class_stage
    is_active = None
    created_by = request.user
    if request.method == "POST":
        if "name" in request.POST:
            name = request.POST["name"]
        if "is_active" in request.POST:
            is_active = request.POST["is_active"]
        add_study_term = School_study_terms(study_term_name=name, study_term_stage=stage,study_term_class=Class, study_term_is_active=is_active, study_term_created_by=created_by)
        add_study_term.save()
    return render(request, "study_section/study_terms.html", {
        "study_terms": study_terms
    })


def subjects(request, pk):
    study_term = School_study_terms.objects.get(pk=pk)
    subjects = School_subjects.objects.filter(
        subject_study_term=study_term, subject_is_active=True)
    name = None
    stage = study_term.study_term_stage
    Class = study_term.study_term_class
    is_active = None
    created_by = request.user
    if request.method == "POST":
        if "name" in request.POST:
            name = request.POST["name"]
        if "is_active" in request.POST:
            is_active = request.POST["is_active"]
        add_subject = School_subjects(subject_name=name, subject_stage=stage, subject_class=Class,
                                      subject_study_term=study_term, subject_is_active=is_active, subject_created_by=created_by)
        add_subject.save()
    return render(request, "study_section/subjects.html", {
        "subjects": subjects,
    })


def units(request, pk):
    subject = School_subjects.objects.get(pk=pk)
    units = School_units.objects.filter(
        unit_subject=subject, unit_is_active=True)
    name = None
    stage = subject.subject_stage
    Class = subject.subject_class
    study_term = subject.subject_study_term
    is_active = None
    created_by = request.user
    if request.method == "POST":
        if "name" in request.POST:
            name = request.POST["name"]
        if "is_active" in request.POST:
            is_active = request.POST["is_active"]
        add_unit = School_units(unit_name=name, unit_stage=stage, unit_class=Class, unit_study_term=study_term,
                                unit_subject=subject, unit_is_active=is_active, unit_created_by=created_by)
        add_unit.save()
    return render(request, "study_section/units.html", {
        "units": units
    })


def lessons(request, pk):
    unit = School_units.objects.get(pk=pk)
    lessons = School_lessons.objects.filter(
        lesson_unit=unit, lesson_is_active=True)
    name = None
    stage = unit.unit_stage
    Class = unit.unit_class
    study_term = unit.unit_study_term
    subject = unit.unit_subject
    is_active = None
    created_by = request.user
    if request.method == "POST":
        if "name" in request.POST:
            name = request.POST["name"]
        if "is_active" in request.POST:
            is_active = request.POST["is_active"]
        add_lesson = School_lessons(lesson_name=name, lesson_stage=stage, lesson_class=Class, lesson_study_term=study_term,
                                    lesson_subject=subject, lesson_unit=unit, lesson_is_active=is_active, lesson_created_by=created_by)
        add_lesson.save()
    return render(request, "study_section/lessons.html", {
        "lessons": lessons
    })


def lesson(request, pk):
    lesson = School_lessons.objects.get(pk=pk)
    docx_urls = Lessons_urls.objects.filter(
        url_type="docx", url_lesson=lesson, url_is_active=True)
    pdf_urls = Lessons_urls.objects.filter(
        url_type="pdf", url_lesson=lesson, url_is_active=True)
    audio_urls = Lessons_urls.objects.filter(
        url_type="audio", url_lesson=lesson, url_is_active=True)
    vidio_urls = Lessons_urls.objects.filter(
        url_type="vidio", url_lesson=lesson, url_is_active=True)
    docx_files = Lessons_files.objects.filter(
        file_type="docx", file_lesson=lesson, file_is_active=True)
    pdf_files = Lessons_files.objects.filter(
        file_type="pdf", file_lesson=lesson, file_is_active=True)
    audio_files = Lessons_files.objects.filter(
        file_type="audio", file_lesson=lesson, file_is_active=True)
    vidio_files = Lessons_files.objects.filter(
        file_type="vidio", file_lesson=lesson, file_is_active=True)
    if request.method == "POST":
        stage =lesson.lesson_stage
        Class =lesson.lesson_class
        study_term =lesson.lesson_study_term
        subject =lesson.lesson_subject
        unit =lesson.lesson_unit
        created_by =request.user
        if "url_name" and "url_type" and "url" and "url_is_active" in request.POST:
            url_name =request.POST ["url_name"]
            url_type =request.POST ["url_type"]
            url =request.POST ["url"]
            url_is_active =request.POST ["url_is_active"]
            add_url =Lessons_urls(url_name=url_name,url_type=url_type,url_stage=stage,url_class=Class,url_study_term=study_term,url_subject=subject,url_unit=unit,url_lesson=lesson,url_is_active=url_is_active,url_created_by=created_by)
            add_url.save ()
        if "file_name" and "file_type" and "file" and "file_is_active" in request.POST:
            file_name =request.POST ["file_name"]
            file_type =request.POST ["file_type"]
            file =request.POST ["file"]
            file_is_active =request.POST ["file_is_active"]
            add_file =Lessons_files(file_name=file_name,file_type=file_type,file_stage=stage,file_class=Class,file_study_term=study_term,file_subject=subject,file_unit=unit,file_lesson=lesson,file_is_active=file_is_active,file_created_by=created_by)
            add_file.save ()
    return render(request, "study_section/lesson.html", {
        "lesson": lesson,
        "docx_urls": docx_urls,
        "pdf_urls": pdf_urls,
        "audio_urls": audio_urls,
        "vidio_urls": vidio_urls,
        "docx_files": docx_files,
        "pdf_files": pdf_files,
        "audio_files": audio_files,
        "vidio_files": vidio_files,
    })
