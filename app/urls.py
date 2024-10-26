from . import views
from django.urls import path

app_name = "app"

urlpatterns = [
    path("",view = views.TodoIndexView.as_view(),name="home"),
    path("task/<int:pk>/",view = views.FullDetailView.as_view(),name="task-detail"),
    path('task/<int:pk>/delete/', views.PostDeletelView.as_view(), name='task-delete'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path("task/<int:pk>/complete/", views.MarkTaskCompletedView.as_view(), name="task-complete"),
    path("task/<int:pk>/incomplete/", views.MarkTaskIncompletedView.as_view(), name="task-incomplete"),
    path('task/new/', views.TaskCreateView.as_view(), name='task-create'),

    
]