from django.db import models
from django.contrib.auth.models import AbstractUser

class Make(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to='car_images/', default='')
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def total_expenses(self):
        total_expenses = sum(expense.price for expense in self.expenses.all())
        return total_expenses

    @property
    def total_price(self):
        return self.buying_price + self.total_expenses

    def __str__(self):
        return f"{self.make} {self.model}"

class Document(models.Model):
    car = models.ForeignKey(Car, related_name='documents', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='car_documents/')

    def __str__(self):
        return self.name

class Expense(models.Model):
    car = models.ForeignKey(Car, related_name='expenses', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

