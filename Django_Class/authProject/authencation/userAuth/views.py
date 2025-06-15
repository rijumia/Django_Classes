from django.shortcuts import render


def registration(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')