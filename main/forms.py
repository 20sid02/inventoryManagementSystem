from django import forms
from .models import products, inventory, inventory_transactions

class createProductForm(forms.ModelForm):
    name = forms.CharField(max_length=256, label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Product Name'}))

    sku = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'SKU'}))

    cost_price = forms.DecimalField(label='', widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Cost Price'}))

    selling_price = forms.DecimalField(label='', widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Selling Price'}))

    reorder_level = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Reorder Level'}))

    class Meta:
        model = products
        fields = ('name', 'sku', 'cost_price', 'selling_price', 'reorder_level')
    
    def __init__(self, *args, **kwargs):
        super(createProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Product Name'
        self.fields['name'].label = ''
        self.fields['name'].help_text = '<span class="form-text text-muted"><small>Required. Add products with full name. Replace spaces between words with /-/, else remove spaces.</small></span>'

        self.fields['sku'].widget.attrs['class'] = 'form-control'
        self.fields['sku'].widget.attrs['placeholder'] = 'SKU'
        self.fields['sku'].label = ''
        self.fields['sku'].help_text = '<span class="form-text text-muted"><small>Required. SKU followed by numerical sequence.</small></span>'
        

class transactionsForm(forms.ModelForm):
    class Meta:
        model = inventory_transactions
        fields = ['product', 'change_type', 'quantity']
