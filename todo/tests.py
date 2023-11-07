from django.test import TestCase

from datetime import datetime

from .models import TodoItem, TodoList

class TodoTestCase(TestCase):
    
    DUMMY_TODO_TITLE = "Test TodoItem"
    
    def setUp(self):
        self.todoList = TodoList(name="Test TodoList")
        self.todoList.save()
        self.todoItem = TodoItem(title=self.DUMMY_TODO_TITLE, due_date=datetime.today(), completed=True, favorite=False, liste=self.todoList)
        self.todoItem.save()
        
    def test_create_todo(self):
        # Voir combien sont present dans notre BD(todoItem)
        nbr_todo_before = TodoItem.objects.count()
        # Aouter un todoItem dans la BD
        new_todo = TodoItem(title="Acheter de l'eau", due_date=datetime.today(), completed=False, favorite=True, liste=self.todoList)
        new_todo.save()
        # Verifier que le nombre a augmente de 1
        nbr_todo_after = TodoItem.objects.count()
        self.assertEqual(nbr_todo_before + 1, nbr_todo_after)
     
    def test_update_todo(self):
        
        self.assertEqual(self.todoItem.title, self.DUMMY_TODO_TITLE) # Voir si le titre est bien celui qu'on a mis dans le setUp
        self.todoItem.title = "Test TodoItem Updated"
        self.todoItem.save()
        self.assertEqual(self.todoItem.title, "Test TodoItem Updated")
        
        
    def test_delete_todo_item(self):
        # Voir combien sont present dans notre BD(todoItem)
        nbr_todo_before = TodoItem.objects.count()
        # Supprimer un todoItem dans la BD
        self.todoItem.delete()
        # Verifier que le nombre a diminue de 1
        nbr_todo_after = TodoItem.objects.count()
        self.assertEqual(nbr_todo_before - 1, nbr_todo_after)    