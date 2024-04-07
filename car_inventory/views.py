from django.shortcuts import get_object_or_404, render, redirect
from .models import Car, Document, Expense
from .forms import CarForm, DocumentForm, ExpenseForm,UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# shared views
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:  # Check if user is admin
                return redirect('admin_panel')  # Redirect to admin site
            else:
                return redirect('car_list')  # Redirect to home page for regular users
    return render(request, 'car_inventory/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

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




def car_detail_admin(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'admin_files/car_detail_admin.html', {'car': car})

# normal user views
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


# admin views


def admin_panel(request):
    return render(request, 'admin_files/dashboard.html')

def dashboard(request):
    car_count = Car.objects.count()
    user_count = User.objects.count()
    return render(request, 'admin_files/dashboard.html', {'car': car_count, 'user': user_count})


def car_list_admin(request):
    cars = Car.objects.all()
    return render(request, 'admin_files/car_list.html', {'cars': cars})

def edit_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'admin_files/edit_car.html', {'form': form, 'car': car})

def delete_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'car_list.html', {'car': car})


def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password1']
            confirm_password = form.cleaned_data['password2']
            if password == confirm_password:
                form.save()
                return redirect('user_list')
            else:
                # Passwords don't match, display error message
                form.add_error('password2', 'Passwords do not match')
    else:
        form = UserCreationForm()
    return render(request, 'admin_files/add_user.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'admin_files/edit_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'admin_files/user_list.html', {'user': user})

def user_list(request):
    users = User.objects.all()
    return render(request, 'admin_files/manage_users.html', {'users': users})

def car_gallery(request):
    cars = Car.objects.all()
    return render(request, 'admin_files/car_gallery.html', {'cars': cars})

