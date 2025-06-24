from django.shortcuts import render,redirect
from customUsersApp.models import customUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def loginPage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def signupPage(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Confirm_Password = request.POST.get('Confirm_Password')
        role = request.POST.get('role')

        if Password == Confirm_Password:
            user = customUser.objects.create_user(
                username=Username,
                email=Email,
                password=Confirm_Password,
                user_type=role,
            )
            return redirect('loginPage')
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match!'})

    return render(request, 'signup.html')


def homePage(request):
    return render(request, 'home.html')
