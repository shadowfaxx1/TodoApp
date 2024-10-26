from django.shortcuts import render,redirect
from django.views import generic
from .models import Task,content
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.forms import BaseModelForm
from django.shortcuts import get_object_or_404
from .forms import TaskCreateForm
from django.urls import reverse, reverse_lazy
from django.views import View

class TodoIndexView(generic.ListView):
    template_name = 'app/home.html'
    context_object_name = 'all_todo_items'
    model = Task
    # def get_queryset(self):
    #     return Task.objects.filter(published_date__lte = timezone.now())[:5]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_tasks'] = Task.objects.filter(is_completed=True)  
        return context
    
    
class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'app/task_form.html'
    success_url = '/'

    def form_valid(self, form):
        task = form.save(commit=False)  # Save the task but don't commit yet
        task.save()  # Now save the task instance
        
        # Create the content instance with the description from the form
        content_instance = content(task=task, description=form.cleaned_data['description'])
        content_instance.save()  # Save the content instance
        
        return super().form_valid(form)


class FullDetailView(generic.DetailView):
    template_name = 'app/detail.html'
    context_object_name=  'context'
    model = Task

class PostDeletelView(generic.DeleteView): #LoginRequiredMixin,UserPassesTestMixin,
    model = Task
    success_url = '/'
    template_name = 'app/confirm_delete.html'  

    def test_func(self) -> bool:
        return True
    # def test_func(self) -> bool:
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

class MarkTaskCompletedView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = True  
        task.save()
        return redirect('app:home')  
    
class MarkTaskIncompletedView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = False  
        task.save()
        return redirect('app:home')  































    
class TaskUpdateView(generic.UpdateView):# LoginRequiredMixin,UserPassesTestMixin
    success_url='/'
    model = Task
    fields = ['title', 'due_date',]
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        # form.instance.author= self.request.user
        return super().form_valid(form)
    def test_func(self) -> bool:
        return True
        # post = self.get_object()
        # if self.request.user == post.author:
        #     return True
        # return False   
    
# class PostCreateView(LoginRequiredMixin,CreateView):
#     model = Post
#     fields = ['title', 'content']
#     def form_valid(self, form: BaseModelForm) -> HttpResponse:
#         form.instance.author= self.request.user
#         return super().form_valid(form)
