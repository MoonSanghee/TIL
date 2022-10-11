from django.shortcuts import render, redirect

from accounts.models import User
from .forms import UsersForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'accounts/home.html', context)

def signup(request):
    if  request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('accounts:home')
    else:
        form = UsersForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    context = {
        'user1': User.objects.get(pk=pk)
    }
    return render(request, 'accounts/detail.html', context)

def userlist(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, 'accounts/userlist.html', context)