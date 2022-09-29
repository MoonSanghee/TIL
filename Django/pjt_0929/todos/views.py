from django.shortcuts import redirect, render
from .models import todos

# Create your views here.
def index(request):
    needs = todos.objects.all().order_by('-priority')
    context = {
        'todos' : needs
    }
    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    todos.objects.create(content=content,priority=priority,deadline=deadline)
    return redirect('todos:index')

def delete(request, pk):
    kill = todos.objects.get(id=pk)
    kill.delete()
    return redirect('todos:index')

def edit(request, pk):
    change = todos.objects.get(id=pk)
    context = {
        'todo' : change,
    }

    return render(request, 'todos/edit.html', context)

def change(request, pk):
    change = todos.objects.get(id=pk)
    
    if change.completed == True:
        change.completed = False
    elif change.completed == False:
        change.completed = True
    
    change.save()
    return redirect('todos:index')


def update(request, pk):
    todo = todos.objects.get(pk=pk)

    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    completed = request.GET.get('completed')

    todo.content = content
    todo.priority = priority
    todo.deadline = deadline
    todo.completed = completed

    todo.save()
    return redirect('todos:index')