from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="home"),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
    path('add/', views.TaskCreateView.as_view(), name='add'),
    path('edit/<int:pk>/', views.TaskEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
    
]