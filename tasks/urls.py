from django.urls import path
from .views import (
    RegisterView,
    TaskListCreateView,
    TaskDetailView,
    MarkCompleteView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', MarkCompleteView.as_view(), name='mark-complete'),
]
