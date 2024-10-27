from django import forms
from .models import Task
from django.utils import timezone
from django.core.exceptions import ValidationError

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
