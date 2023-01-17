from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class Add_post_form (ModelForm):
    class Meta:
        model =Forums
        fields ="__all__"