from django.http import request

from . models import Task
from django import forms

class Todoform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']
