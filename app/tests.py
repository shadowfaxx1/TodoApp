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
        task = create_question(title="Future question.", due_date=5,description="zoozoo")
        response = self.client.get('/')  

        self.assertEqual(response.status_code, 200)  
        self.assertIn(task, response.context['all_todo_items']) 
        task_in_response = next(
            item for item in response.context['all_todo_items'] if item.id == task.id
        )
        self.assertTrue(task_in_response.due_date < task_in_response.published_date)
        self.assertIs(task_in_response.due_date < task_in_response.published_date, False)

    def test_due_date_lesser_than_published_date(self):
        with self.assertRaises(ValidationError):
            Task.objects.create(
                title='Test Task 2',
                due_date=timezone.now() - timezone.timedelta(days=1),  # Invalid past date
                description='This should fail',
                author=self.user 
            )


    def test_title_length(self):
        task = Task(title='A' * 101, due_date=timezone.now() + timezone.timedelta(days=1), description='Too long title', author=self.user)
        with self.assertRaises(ValidationError):
            task.full_clean() 

    def test_description_length(self):
        task = Task(title="Valid Title", description="123456", published_date=timezone.now(), due_date=timezone.now() + timezone.timedelta(days=1))
        
        with self.assertRaises(ValidationError) as context:
            task.clean()  
        self.assertEqual(str(context.exception), "['Description must be at least 10 characters long.']")

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.task1 = Task.objects.create(
            title='Test Task 1',
            due_date=timezone.now() + timezone.timedelta(days=1), 
            description='This is a test task',
            author=self.user  # Set the author to the created user
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('app:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/home.html')
        self.assertContains(response, 'Test Task 1')
        self.assertContains(response, 'Test Task 2')
        self.assertQuerysetEqual(
            response.context['all_todo_items'],
            Task.objects.filter(author=self.user).order_by('due_date')[:5]
        )

    def test_task_create_view(self):
        response = self.client.post(reverse('app:task_create'), {
            'title': 'New Task',
            'due_date': '2024-12-03 12:00:00',
            'description': 'New task description',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_update_view(self):
        response = self.client.post(reverse('app:task_update', args=[self.task1.id]), {
            'title': 'Updated Task',
            'due_date': '2024-12-04 12:00:00',
            'description': 'Updated description',
        })
        self.assertEqual(response.status_code, 302) 
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')

    def test_task_delete_view(self):
        response = self.client.post(reverse('app:task_delete', args=[self.task1.id]))
        self.assertEqual(response.status_code, 302)  
        self.assertFalse(Task.objects.filter(id=self.task1.id).exists())

    def test_mark_task_completed_view(self):
        response = self.client.post(reverse('app:mark_task_completed', args=[self.task1.id]))
        self.assertEqual(response.status_code, 302) 
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.is_completed)

    def test_mark_task_incompleted_view(self):
        response = self.client.post(reverse('app:mark_task_incompleted', args=[self.task2.id]))
        self.assertEqual(response.status_code, 302)  
        self.task2.refresh_from_db()
        self.assertFalse(self.task2.is_completed)

