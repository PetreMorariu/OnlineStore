from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from . forms import ProductForm
from . models import Product
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request,'onlinestore/home.html', {'products':products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'The product was added!')
            return redirect('store-home')
        else:
            messages.error(request, f'Please correct the errors')
            return render(request,'onlinestore/add_product.html',{'form':form})
    else:
        form = ProductForm()
        return render(request,'onlinestore/add_product.html',{'form':form})
