from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoSerializer
from .forms import TodoForm

def todo_list(request):
    items = TodoItem.objects.all().order_by('-date')
    return render(request, 'todo/todo_list.html', {'items': items})

def add_todo_item(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/add_todo_item.html', {'form': form})

def update_todo_item(request, id):
    item = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=item)
    return render(request, 'todo/update_todo_item.html', {'form': form})

def delete_todo_item(request, id):
    item = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('todo_list')
    return render(request, 'todo/confirm_delete.html', {'item': item})

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer
