from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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

def get_all_users(request):
    users = UserDetails.objects.all().values('username', 'email', 'password')
    return JsonResponse(list(users), safe=False)

def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        return JsonResponse({
            'username': user.username,
            'email': user.email,
            'password': user.password,
        })
    except UserDetails.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
@csrf_exempt
def update_user(request, email):
    if request.method == 'POST':
        try:
            user = UserDetails.objects.get(email=email)
            data = json.loads(request.body)  # Parse JSON data
            user.username = data.get('username', user.username)
            user.password = data.get('password', user.password)
            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def delete_user(request, email):
    if request.method == 'DELETE':
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)