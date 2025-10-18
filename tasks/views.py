from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]



class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['due_date', 'priority']
    search_fields = ['status', 'priority']

    def get_queryset(self):
        # Only return the logged-in user's tasks
        user = self.request.user
        queryset = Task.objects.filter(user=user)

        # Optional filters: ?status=Completed&priority=High
        status_param = self.request.query_params.get('status')
        priority_param = self.request.query_params.get('priority')

        if status_param:
            queryset = queryset.filter(status=status_param)
        if priority_param:
            queryset = queryset.filter(priority=priority_param)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        task = self.get_object()
        if task.status == 'Completed' and self.request.data.get('status') != 'Pending':
            return Response(
                {"error": "Cannot edit a completed task unless reverted to Pending."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()


class MarkCompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        status_param = request.data.get('status', None)

        if status_param == 'Completed':
            task.status = 'Completed'
            task.completed_at = timezone.now()
        elif status_param == 'Pending':
            task.status = 'Pending'
            task.completed_at = None
        else:
            return Response({"error": "Invalid status. Use 'Completed' or 'Pending'."}, status=status.HTTP_400_BAD_REQUEST)

        task.save()
        return Response({"message": f"Task marked as {task.status}."}, status=status.HTTP_200_OK)
