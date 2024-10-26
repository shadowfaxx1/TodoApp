from django import forms
from .models import Task, content
import datetime 
from django.utils import timezone 
 



class TaskCreateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'description']