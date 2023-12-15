# forms.py
from django import forms
from accounts.models import Jobs


class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['job_title', 'job_description',
                  'salary', 'vacancy', 'status']
