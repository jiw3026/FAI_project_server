from django import forms
from .models import *

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ['user_id', 'diag_image']