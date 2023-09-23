from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import User, Province, City, District, Street
from django.http import HttpResponse


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        error = None
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Username or password not correct"
            return render(request, "login.html", {"error": error})
    return render(request, "login.html")


@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect("login")


def register(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        bday = request.POST.get("bday")
        identify_card = request.POST.get("identify_card")

        if password == confirm_password:
            try:
                user = User.objects.get(username=username)
                if user:
                    error = "User already existed"
                    return render(request, "register.html", {"error": error})
            except:
                user = User(
                    username=username,
                    password=make_password(password),
                    bday=bday,
                    identify_card=identify_card,
                )
                user.save()
                return redirect("login")

        error = "Password and confirm password are different"
        return render(request, "register.html", {"error": error})

    return render(request, "register.html")


def profile(request):
    try:
        user = User.objects.get(id=request.user.id)
        return render(request, "profile.html", {"user": user})
    except:
        return redirect("home")


def update_profile(request):
    provincies = Province.objects.all()
    cities = City.objects.all()
    districts = District.objects.all()
    streets = Street.objects.all()
    try:
        user = User.objects.get(id=request.user.id)

        if request.method == "POST":
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            identify_card = request.POST["identify_card"]
            phone = request.POST["phone"]
            mobile = request.POST["mobile"]
            province = request.POST["province"]
            city = request.POST["city"]
            district = request.POST["district"]
            street = request.POST["street"]
            user.firstname = firstname
            user.lastname = lastname
            user.identify_card = identify_card
            user.phone = phone
            user.mobile = mobile
            user.province = province
            user.city = city
            user.district = district
            user.street = street
            user.save()
            return HttpResponse("aaa")

        return render(
            request,
            "update_profile.html",
            {
                "user": user,
                "provincies": provincies,
                "cities": cities,
                "districts": districts,
                "streets": streets,
            },
        )

    except:
        return redirect("home")
