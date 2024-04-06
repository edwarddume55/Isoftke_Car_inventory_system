from django import forms
from .models import Car, Document, Expense
# from django.contrib.auth.forms import UserCreationForm


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
        


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password1', 'password2', 'is_customer', 'is_employee']