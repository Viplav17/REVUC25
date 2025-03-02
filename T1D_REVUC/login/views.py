from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'login/home.html')

def signup(request):
    if request.method == 'POST':
        # Extract form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validate password match
        if password != confirm_password:
            return HttpResponse('Passwords do not match! Please try again.')

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already exists! Please choose another one.')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Log the user in
        auth_login(request, user)

        # Redirect to home page
        return redirect('home')

    return render(request, 'login/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Correct method to log the user in
            auth_login(request, user)
            return redirect('home')  # Redirect to a dashboard or home page after login
        else:
            return HttpResponseForbidden('Invalid credentials or CSRF token error.')

    return render(request, 'login/login.html')  # Ensure the template is correct
