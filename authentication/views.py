from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        breakpoint()
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Wrong username or password'))
            return redirect('login')
    
    return render(request, 'login.html')
