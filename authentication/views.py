from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from . import models



@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Wrong username or password'))
            return redirect('login')

    return render(request, 'login.html')


@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        bday = request.POST.get('bday')
        identify_card = request.POST.get('identify_card')
        breakpoint()
        user = models.User(username=username, password=password, bday=bday,identify_card=identify_card)
        user.save()
        return redirect('login')
    
    return render(request, 'register.html')
