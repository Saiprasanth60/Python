from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Use to create the username
from django.contrib.auth.models import User  # Use for adding data into DB
from django.db import IntegrityError  # Check the username exit in db or not
from django.contrib.auth import login, logout, authenticate
from .forms import todoform
from .models import todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm()})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodo')

            except IntegrityError:
                return render(request, 'signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Username already take'})
        else:
            return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Password didnt match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password didnt match'})
        else:
            login(request, user)
            return redirect('currenttodo')


@login_required
def currenttodo(request):
    todosdata = todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'current.html', {'todosdata': todosdata})


@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'createtodo.html', {'form': todoform()})
    else:
        try:
            form = todoform(request.POST)
            newtodo = form.save(commit=False)  # commit = false used not to commit unless it is true
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'createtodo.html', {'form': todoform(), 'error': 'Try again'})


@login_required
def tododetailview(request, todo_pk):
    todoallobject = get_object_or_404(todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = todoform(instance=todoallobject) #todoform have some required objects for that objects values will be taken from todoallobject
        return render(request, 'todoview.html', {'todoallobject':todoallobject, 'form':form})
    else:
        try:
            form = todoform(request.POST,instance=todoallobject)
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todoview.html', {'todoallobject':todoallobject, 'form':form, 'error':'Try again'})


@login_required
def completetodo(request, todo_pk):
    todoallobject = get_object_or_404(todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todoallobject.datecompleted = timezone.now()
        todoallobject.save()
        return redirect('currenttodo')


@login_required
def listofcompletedtodo(request):
    todosdata = todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'listofcompletedtodo.html', {'todosdata': todosdata})


@login_required
def deletetodo(request, todo_pk):
    todoallobject = get_object_or_404(todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todoallobject.delete()
        return redirect('currenttodo')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
