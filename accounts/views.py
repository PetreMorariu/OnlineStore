from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm

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


