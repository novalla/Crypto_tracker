from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.db import IntegrityError
from .models import *



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page upon successful login
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'portfolio/login.html', {'error_message': error_message})
    
    return render(request, 'portfolio/login.html')
    
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            try:
                # Create a new user object
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')  # Redirect to the login page after successful registration
            except IntegrityError:
                error_message = 'Username is already taken. Please choose a different username.'
                return render(request, 'portfolio/registration.html', {'error_message': error_message})
        else:
            error_message = 'Passwords do not match. Please try again.'
            return render(request, 'portfolio/registration.html', {'error_message': error_message})
    
    return render(request, 'portfolio/registration.html')

    
    return render(request, 'portfolio/registration.html')
# @login_required
# def dashboard(request):
#     user = request.user.username
#     print("printing the user that currently login into the dashboard ")
#     print(user)
#     # cryptocurencies = Cryptocurrency.objects.all()
#     cryptocurencies = Portfolio.objects.get(user=request.user)
#     return render(request, 'portfolio/dashboard.html', {'cryptocurencies': cryptocurencies, 'user': user})



def home(request):
    portfolio = Cryptocurrency.objects.all()
    return render(request, 'portfolio/home.html', {'portfolio': portfolio})
   

    
@login_required
def add_to_portfolio(request):
    if request.method == "POST":
        crypto_symbols = request.POST.getlist('crypto_symbol')
        portfolio, created = Portfolio.objects.get_or_create(user=request.user)

        added_cryptos = []
        existing_cryptos = []

        for symbol in crypto_symbols:
            cryptocurrency = Cryptocurrency.objects.filter(symbol=symbol).first()
            if cryptocurrency:
                if not portfolio.cryptocurrencies.filter(symbol=symbol).exists():
                    portfolio.cryptocurrencies.add(cryptocurrency)
                    added_cryptos.append(cryptocurrency.name)
                else:
                    existing_cryptos.append(cryptocurrency.name)

        messages = []
        if added_cryptos:
            messages.append(f"Added: {', '.join(added_cryptos)}")
        if existing_cryptos:
            messages.append(f"Already in portfolio: {', '.join(existing_cryptos)}")

        if added_cryptos or existing_cryptos:
            return redirect('dashboard')

    return render(request, 'portfolio/add_to_portfolio.html', {
        'cryptocurrencies': Cryptocurrency.objects.all()
    })

@login_required
def dashboard(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
        cryptocurrencies = portfolio.cryptocurrencies.all()
    except Portfolio.DoesNotExist:
        cryptocurrencies = None

    context = {
        'cryptocurrencies': cryptocurrencies,
        'user': request.user.username,
    }

    return render(request, 'portfolio/dashboard.html', context)

def custom_logout_view(request):
    logout(request)
    return redirect('login')