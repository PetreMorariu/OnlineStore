from django.shortcuts import render

products = [
    {
        'name':"Car",
        'description':"Description for the Car",
        'price': 12.23,
        'stock':20
    },
    {
        'name': "Bike",
        'description': "Description for the Bike",
        'price': 2.23,
        'stock': 25
    }
]

def home(request):
    context = {
        'products': products
    }
    return render(request,'onlinestore/home.html',context)