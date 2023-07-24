from django.db import models
from django.urls import reverse
from django.utils import timezone


# function for the time zone now to seven day later
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# Create your models here.

class ToDoList(models.Model):
    title = models.CharField(max_length=264,unique=True)
    def get_absolute_url(self):
        return reverse('list',args=[self.id])
    def __str__(self):
        return self.title

class ToDoItems(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    # method for getting the absolute url
    def get_absolute_url(self):
        return reverse('item_update',args=[str(self.todo_list.id),str(self.id)])
    # get the name of the tast
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['due_date']