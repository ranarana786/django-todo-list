from django.contrib import admin
from .models import ToDoList,ToDoItems

# Register your models here.

# Admin for the todolist table
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(ToDoList,ToDoListAdmin)

# Admin for the todolist table
class ToDoItemsAdmin(admin.ModelAdmin):
    list_display = ['title','description','created_date','due_date','todo_list']
admin.site.register(ToDoItems,ToDoItemsAdmin)

