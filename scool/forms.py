from django import forms
from .models import *


class School_sections_form (forms.Form):
    class Meta:
        modle =Scool_sections
        fealds =["section_name","section_stage","section_class","section_is_active","section_created_by"]