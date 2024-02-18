from django import forms
from . import models

class stuform(forms.ModelForm):
    class Meta():
        model = models.student
        fields = '__all__'