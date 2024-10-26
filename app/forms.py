from django import forms
from .models import Task, content
import datetime 
from django.utils import timezone 

class TaskContentForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Task
        fields = ['title', 'due_date']  

class ContentForm(forms.ModelForm):
    class Meta:
        model = content
        fields = ['description']  