from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from tasks.views import (
    RegisterView,
    TaskListCreateView,
    TaskDetailView,
    MarkCompleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('api/tasks/<int:pk>/complete/', MarkCompleteView.as_view(), name='mark-complete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
