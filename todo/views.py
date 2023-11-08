from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import TodoItem, TodoList
from .serializers import TodoItemSerializer, TodoListSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['due_date', 'completed', 'favorite']
    search_fields = ['title']
    
class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer   
    permission_classes = [IsAuthenticated] 