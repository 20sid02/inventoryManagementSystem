from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('viewInventory/', views.viewInventory, name='viewInventory'),
    path('transactions/', views.processTransactions, name='transactions'),
    path('recentTransactions/', views.transHistory, name='recentTransactions'),
]