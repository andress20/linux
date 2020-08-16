from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from .forms import TodoForm

def todoList(request):
    tList = TodoItem.objects.all()

    formAdd = TodoForm(request.POST or None)

    if request.method == 'POST':
        #formAdd = TodoForm(request.POST or None)
        if formAdd.is_valid():
            formAdd.save()
            return redirect('/todo/')
    context ={
        'tList': tList, 'formAdd': formAdd, 
    }

    return render(request, 'todo.html', context)