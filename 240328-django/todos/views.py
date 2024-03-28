from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos,
    }
    return render(request, 'todos/index.html', context)


def create(request):
    title = request.POST.get('title')
    todo = Todo(title = title)
    # 유효성 검사

    todo.save() # 생성 쿼리 실행

    return redirect('todos:index')


def new(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    context = {
        'form' : form
    }
    return render(request, 'todos/new.html', context)

def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo' : todo
    }
    return render(request, 'todos/detail.html', context)

def delete(request, pk):
    # 조회하고 삭제하고 목록 보여주기
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect('todos:index')

def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:index')

def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.is_editting:
        todo.is_editting  = False
    else:
        todo.is_editting = True
    return redirect('todos:index')