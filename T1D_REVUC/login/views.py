from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login


def home(request):
    return render(request, 'login/home.html')

def signup(request):
    if request.method == 'POST':
        # Extract form data
        username = request.POST['username']
        email = request.POST['email']
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
        login(request, user)
        
        # Redirect to a success page or home page
        return redirect('home')  # Adjust this to your success page or home view

    return render(request, 'login/signup.html')