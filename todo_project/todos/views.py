from django.shortcuts import render
from django.http import request
from .forms import TodoForm
# Create your views here.
from .models import Todo


def index(request):

    # form?
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        # check for validity of the form
        if form.is_valid():
            # create the instance of a Todo
            todo = form.save()

    # check whether we are doing a POST or GET?
    # Get all the todos 
    todos = Todo.objects.all()

    return render(request, 'todos/index.html' ,{"form": form, "todos": todos})