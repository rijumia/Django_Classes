from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from task_App.models import CustomUserModel, TaskModel

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
    return render(request, 'login.html')

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        img = request.FILES.get('img')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            CustomUserModel.objects.create_user(
                username = username,
                first_name = fullname,
                email = email,
                profile_picture = img,
                bio = bio,
                password = password,
            )
            return redirect('loginPage')
    return render(request, 'register.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def homePage(request):
    return render(request, 'home.html')


