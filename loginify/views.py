from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails


# Test view to display "Hello, world!"
def test_view(request):
    return HttpResponse("Hello, world!")

# Login view
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check if the user exists
            user = UserDetails.objects.get(email=email, password=password)
            return HttpResponse(f"Welcome, {user.username}! Login successful.")
        except UserDetails.DoesNotExist:
            return HttpResponse("Invalid email or password!")

    return render(request, 'loginify/login.html')

# Signup view
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Ensure email is unique
        if UserDetails.objects.filter(email=email).exists():
            return HttpResponse("Email already exists!")

        # Save the new user
        UserDetails.objects.create(username=username, email=email, password=password)
        return redirect('login_view')  # Redirect to the login page upon successful signup

    return render(request, 'loginify/signup.html')