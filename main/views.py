from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import createProductForm, transactionsForm
from .models import products, inventory, inventory_transactions

def index(request):
    products_rec = products.objects.all()
    inventory_transactions_rec = inventory_transactions.objects.all() 
    return render(request, 'index.html', {'products_rec' : products_rec, 'inventory_transactions_rec' : inventory_transactions_rec})

def addProduct(request):
    form = createProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            prod = form.save()
            change_type = form.cleaned_data.get('change_type')
            quantity = form.cleaned_data.get('quantity') or 0

            if change_type and quantity > 0:
                inventory_transactions.objects.create(product=prod, change_type=change_type, quantity=quantity)
            messages.success(request, 'Product added successfully')
            return redirect('index')
    else:
        return render(request, 'addProduct.html', {'form' : form})


def viewInventory(request):
    items = inventory.objects.select_related('product').all()
    return render(request, 'viewInventory.html', {'items' : items})


def processTransactions(request):
    form = transactionsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            trans = form.save()
            messages.success(request, 'Transaction added successfully')
            return redirect('index')
    else:
        return render(request, 'transactions.html', {'form' : form})