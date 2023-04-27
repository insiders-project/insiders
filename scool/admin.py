from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(School_stages)
admin.site.register(School_classes)
class School_sectionsAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "section_class":
            try:
                stage_id = request.resolver_match.kwargs['object_id']
                stage = School_stages.objects.get(pk=stage_id)
                kwargs["queryset"] = School_classes.objects.filter(class_stage=stage)
            except:
                kwargs["queryset"] = School_classes.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(School_sections, School_sectionsAdmin)
admin.site.register(School_study_terms)
admin.site.register(School_subjects)
admin.site.register(School_units)
admin.site.register(School_lessons)