from django.shortcuts import render, redirect
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

class TaskEditView(UpdateView):
    model = Task
    fields = ['title', 'completed']
    template_name = 'todo/edit.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        if 'completed' in request.POST and 'title' not in request.POST:
            task = self.get_object()
            task.completed = 'completed' in request.POST
            task.save()
            return redirect('home')

        return super().post(request, *args, **kwargs)
    

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/delete.html'
    success_url = '/'