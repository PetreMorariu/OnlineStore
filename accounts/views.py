from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created! You can now login!')
            return redirect('store-home')
    else:
        form = UserRegisterForm()
    return render(request,'accounts/register.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store-home')
        else:
            messages.error(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form})