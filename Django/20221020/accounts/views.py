from django.shortcuts import redirect, render
from .forms import CustomCreationUserForm, CustomChangeUserForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def signup(request):
    if request.method =='POST':
        form = CustomCreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomCreationUserForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.')
    return redirect('articles:index')

def detail(request, pk):
    account_detail = get_user_model().objects.get(pk=pk)
    context = {
        'account_detail':account_detail
    }
    return render(request, 'accounts/detail.html', context)

