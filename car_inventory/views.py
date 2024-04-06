from django.shortcuts import get_object_or_404, render, redirect
from .models import Car, Document, Expense
from .forms import CarForm, DocumentForm, ExpenseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required



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

@permission_required('car_inventory.can_manage_cars')
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_inventory/edit_car.html', {'form': form})

@permission_required('car_inventory.can_manage_cars')
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_inventory/delete_car.html', {'car': car})

def add_expense(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.car = car
            expense.save()
            return redirect('car_detail', car_id=car_id)
    else:
        form = ExpenseForm()
    return render(request, 'car_inventory/add_expense.html', {'form': form})

def add_document(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.car = car
            document.save()
            return redirect('car_detail', car_id=car_id)
    else:
        form = DocumentForm()
    return render(request, 'car_inventory/add_document.html', {'form': form, 'car': car})
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:  # Check if user is admin
                return redirect('/admin/')  # Redirect to admin site
            else:
                return redirect('home')  # Redirect to home page for regular users
    return render(request, 'car_inventory/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout