from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "todo/home.html"
    context_object_name = "tasks"

class TaskDetailView(DetailView):
    model = Task
    template_name = "todo/detail.html"

class TaskCreateView(CreateView):
    model = Task
    fields = ['title']
    template_name = 'todo/add.html'
    success_url = '/'