from django.shortcuts import render,reverse
from .models import ToDoList,ToDoItems
from .forms import ToDoListForm,ToDoItemsForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
   all_object = ToDoList.objects.all()
   return render(request,'todoapp/home.html',{'object_list':all_object})

def add_todolist(request):
   form = ToDoListForm()
   if request.method == 'POST':
      form = ToDoListForm(request.POST)
      if form.is_valid():
         data = form.cleaned_data
         ToDoList.objects.get_or_create(title=data['title'].upper())
      home = reverse('index')
      return HttpResponseRedirect(home)
   return render(request,'addtodo_list.html',{'form':form})

def todoitems_views(request,list_id):
   items_data = ToDoItems.objects.filter(todo_list=list_id)
   return render(request,'items.html',{'items_list':items_data})

def todoitems_forms(request):
   form = ToDoItemsForm()
   if request.method == 'POST':
      form = ToDoItemsForm(request.POST)
      if form.is_valid():
          form.save()
          home = reverse('index')
          return HttpResponseRedirect(home)
   return render(request,'todoitems_form.html',{'form':form})
