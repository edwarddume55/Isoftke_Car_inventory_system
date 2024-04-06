from django.shortcuts import get_object_or_404, render, redirect
from .models import Car, Document, Expense
from .forms import CarForm, DocumentForm, ExpenseForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_inventory/car_list.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_inventory/car_detail.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car = car_form.save()
            return redirect('car_detail', car_id=car.id)
    else:
        car_form = CarForm()
    return render(request, 'car_inventory/add_car.html', {'car_form': car_form})

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES, instance=car)
        if car_form.is_valid():
            car_form.save()
            return redirect('car_detail', car_id=car.id)
    else:
        car_form = CarForm(instance=car)
    return render(request, 'car_inventory/edit_car.html', {'car_form': car_form})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_inventory/delete_car.html', {'car': car})
