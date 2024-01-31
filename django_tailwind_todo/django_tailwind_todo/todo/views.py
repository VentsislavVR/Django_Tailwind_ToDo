from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django_tailwind_todo.todo.models import Todo


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }

    return render(
        request,
        'todo/index.html',
        context
    )
@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title', '')

    if title:
        todo = Todo.objects.create(title=title)

    context = {
        'todo': todo
    }
    return render(
        request,
        'partials/todo.html',
        context
    )
@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    title = request.POST.get('title', '')

    todo.is_done = True
    todo.save()

    context = {
        'todo': todo
    }
    return render(
        request,
        'partials/todo.html',
        context)
