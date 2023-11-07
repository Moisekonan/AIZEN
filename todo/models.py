from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=256)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)

    liste = models.ForeignKey('TodoList', null=False, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Todo Item"
        verbose_name_plural = "Todo Items"

    def __str__(self):
        return self.title
    
    
class TodoList(models.Model):
    name = models.CharField(max_length=256)
    
    class Meta:
        verbose_name = "Todo List"
        verbose_name_plural = "Todo Lists"

    def __str__(self):
        return self.name 
    
       