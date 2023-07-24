from django import forms
from .models import ToDoList,ToDoItems

# class ToDoListForm(forms.ModelForm):
#     author = forms.CharField(max_length=20)
#     class Meta:
#         model = ToDoList
#         fields = '__all__'

class ToDoListForm(forms.Form):
    title = forms.CharField(max_length=20)

class ToDoItemsForm(forms.ModelForm):
    class Meta:
        model = ToDoItems
        fields = '__all__'