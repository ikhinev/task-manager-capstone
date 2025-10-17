from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can access

    def get_queryset(self):
        # Return only tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the current user to the task
        serializer.save(user=self.request.user)

    # Custom endpoints for marking tasks complete/incomplete
    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'done'
        task.save()
        return Response({'status': 'Task marked as complete'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'])
    def incomplete(self, request, pk=None):
        task = self.get_object()
        task.status = 'todo'
        task.save()
        return Response({'status': 'Task marked as incomplete'}, status=status.HTTP_200_OK)
