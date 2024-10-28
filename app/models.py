import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
# Create your models here.
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=-5) <= self.published_date

    def clean(self):
        d = self.due_date
        c = (self.published_date)
        c = datetime_obj = datetime.datetime.combine(c, datetime.datetime.min.time())
        d = datetime_obj = datetime.datetime.combine(d, datetime.datetime.min.time())
        
        
        if c > d:
            raise ValidationError("Due date must be greater than or equal to the published date.")
        if len(self.title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")
        if len(self.description) < 10:
            raise ValidationError("Description must be at least 10 characters long.")
        if len(self.title) >20:
            raise ValidationError("Description must be at most 20 characters long.")
            
            
        super().clean()  


    
    
    
    

    
    

    
    
