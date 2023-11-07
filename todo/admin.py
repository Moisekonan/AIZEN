from django.contrib import admin

from .models import TodoItem, TodoList

class TodoItemInline(admin.TabularInline):
    model = TodoItem
    extra = 0

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [TodoItemInline]
    
 
@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'due_date', 'completed', 'favorite', 'liste']
    list_filter = ['due_date', 'completed', 'favorite', 'liste']
    search_fields = ['title']
    