from django.shortcuts import render, redirect
from app.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.forms import *
from app.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import permission_required
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('login')
        context = {'form': form}
        return render (request, 'register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def homepage(request):
    context = {}
    return render(request, 'home.html', context)

def create_show(request):
    form = ShowForm()
    if request.method=='POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            return redirect('home')
    context = {'form': form}
    return render (request, 'create.html', context)

def update_show(request, pk):
    show = Show.objects.get(id=pk)
    form = ShowForm(instance=show)
    if request.method=='POST':
        form = ShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'create.html', context)

def delete_show(request, pk):
    shows = Show.objects.get(id=pk)
    if request.method == 'POST':
        shows.delete()
        return redirect('home')
    context = {'item': shows}
    return render(request, 'delete.html', context)

@allowed_users(allowed_roles=['admin'])
def allusers(request):
    form = Show.objects.all()
    context = {'form': form}
    return render (request, 'all.html', context)

def usertable(request):
    context = {}
    return render (request, 'usertable.html', context)