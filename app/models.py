import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=-5) <= self.published_date

class content(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE) 
    description = models.TextField()
    
    def __str__(self):
        return self.description
    

    
    
    
    

    
    

    
    
