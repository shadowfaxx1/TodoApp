from django.shortcuts import render,redirect
from django.views import generic
from .models import Task
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.forms import BaseModelForm
from django.shortcuts import get_object_or_404
from .forms import TaskCreateForm
from django.urls import reverse, reverse_lazy
from django.views import View
import datetime
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        'all_todo_items': Task.objects.all()
    }
    return render(request, 'app/home.html', context)

class TaskListView(LoginRequiredMixin,generic.ListView):
    template_name = 'app/home.html'
    context_object_name = 'all_todo_items'
    model = Task

    def get_queryset(self):
        return Task.objects.filter(
        author=self.request.user,
        published_date__lte=timezone.now(), 
        is_completed=False
    ).order_by('due_date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_tasks'] = Task.objects.filter(author=self.request.user,is_completed=True)  
        return context
    

class TaskCreateView(LoginRequiredMixin,generic.CreateView):
    model = Task
    # form_class = TaskCreateForm
    template_name = 'app/task_form.html'
    success_url = '/'
    fields = ['title', 'due_date','description']
    

    def form_valid(self, form):
        form.instance.author= self.request.user
        task = form.save(commit=False)
        task.clean()
        task.save()
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    template_name = 'app/task_form.html'
    success_url = '/'
    fields = ['title', 'due_date', 'description']  

    def form_valid(self, form):
        task = form.save(commit=False)
        task.clean()
        task.save()
        return super().form_valid(form)

    def test_func(self) -> bool:
        task = self.get_object()
        return self.request.user == task.author  # Ensure the user is the author


    
class FullDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = 'app/detail.html'
    context_object_name=  'context'
    model = Task
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
    

class PostDeletelView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView): #LoginRequiredMixin,UserPassesTestMixin,
    model = Task
    success_url = '/'
    template_name = 'app/confirm_delete.html'  

    def test_func(self) -> bool:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

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






def about(request):
    return render(request , "app/about.html")

























    
