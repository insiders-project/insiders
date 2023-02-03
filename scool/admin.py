from django.contrib import admin
from .forms import *
from .models import * 

# Register your models here.

admin.site.register(Scool_stages)
admin.site.register(Scool_classes)

class School_sections_admin(admin.ModelAdmin):
    form = School_sections_form

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'section_class':
            kwargs['form_class'] = School_sections_form
            section_stage = request.GET.get('section_stage')
            kwargs['form'] = School_sections_form(section_stage=section_stage)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Scool_sections,School_sections_admin)
admin.site.register(Scool_study_terms)
admin.site.register(Scool_subjects)
admin.site.register(Scool_units)
admin.site.register(Scool_lessons)