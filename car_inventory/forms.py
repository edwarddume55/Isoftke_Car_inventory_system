from django import forms
from .models import Car, Document, Expense

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'car_image', 'buying_price', 'selling_price', 'discount']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'file']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'price']
