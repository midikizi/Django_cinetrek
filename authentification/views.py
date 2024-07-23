from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        role = request.POST.get('role', 'client')  # Default role is 'client'

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        User = get_user_model()
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role=role
        )
        user.save()
        messages.success(request, "User registered successfully.")
        return redirect('login')
    return render(request, 'register.html')