from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('add_product/', views.add_product, name='add_product'),
]