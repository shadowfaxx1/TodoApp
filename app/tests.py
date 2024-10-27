from django.forms import ValidationError
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from .models import Task
from django.urls import reverse


# Create your tests here.
def create_question(title,due_date,description):
    time = timezone.now() + datetime.timedelta(days=-due_date)
    return Task.objects.create(title=title,due_date=time,description=description)

class TasksTestListView(TestCase):
    def test_due_date_lesser_than_published_date(self):
        # Arrange
        task = create_question(title="Future question.", due_date=5,description="zoozoo")
        response = self.client.get('/')  

        self.assertEqual(response.status_code, 200)  
        self.assertIn(task, response.context['all_todo_items']) 
        task_in_response = next(
            item for item in response.context['all_todo_items'] if item.id == task.id
        )
        self.assertTrue(task_in_response.due_date < task_in_response.published_date)
        self.assertIs(task_in_response.due_date < task_in_response.published_date, False)

class TaskModelTests(TestCase):
    
    def test_due_date_cannot_be_less_than_published_date(self):
        future_date = timezone.now() + timezone.timedelta(days=1)
        past_date = timezone.now() - timezone.timedelta(days=1)
        task = Task(title="Valid Title", description="Valid description.", published_date=future_date, due_date=past_date)
        
        with self.assertRaises(ValidationError) as context:
            task.clean()  
        self.assertEqual(str(context.exception), "['Due date must be greater than or equal to the published date.']")

    def test_title_length(self):
        task = Task(title="123", description="Valid description.", published_date=timezone.now(), due_date=timezone.now() + timezone.timedelta(days=1))
        
        with self.assertRaises(ValidationError) as context:
            task.clean()  
        self.assertEqual(str(context.exception), "['Title must be at least 5 characters long.']")

    def test_description_length(self):
        task = Task(title="Valid Title", description="123456", published_date=timezone.now(), due_date=timezone.now() + timezone.timedelta(days=1))
        
        with self.assertRaises(ValidationError) as context:
            task.clean()  
        self.assertEqual(str(context.exception), "['Description must be at least 10 characters long.']")

 
    