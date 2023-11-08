from rest_framework import routers

from .views import TodoItemViewSet, TodoListViewSet

router = routers.DefaultRouter()
router.register('todo', TodoItemViewSet)
router.register('todo-lists', TodoListViewSet)