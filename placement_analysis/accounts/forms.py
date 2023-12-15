# forms.py
from .models import UserModel
from django import forms
from .models import *


class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['resume']


# forms.py


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['resume']
