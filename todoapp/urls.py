from django.urls import path
from . import views
urlpatterns = [
    path('',views.home_view,name = 'index'),
    path('add_todo_list',views.add_todolist,name='add_list'),
    path('item/<int:list_id>',views.todoitems_views,name = 'todoitems'),
    path('add_todo_items',views.todoitems_forms,name='items_form')

]