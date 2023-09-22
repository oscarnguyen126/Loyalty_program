from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import User, Province, City, District, Street


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, ("Wrong username or password"))
            return redirect("login")

    return render(request, "login.html")


@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect("login")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = make_password(request.POST.get("password"))
        bday = request.POST.get("bday")
        identify_card = request.POST.get("identify_card")
        user = User(
            username=username, password=password, bday=bday, identify_card=identify_card
        )
        user.save()
        return redirect("login")

    return render(request, "register.html")


def profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, "profile.html", {"user": user})


def update_profile(request):
    user = User.objects.get(id=request.user.id)
    provincies = Province.objects.all()
    cities = City.objects.all()
    districts = District.objects.all()
    streets = Street.objects.all()

    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        identify_card = request.POST.get("identify_card")
        phone = request.POST.get("phone")
        mobile = request.POST.get("mobile")
        province = request.POST.get("province")
        city = request.POST.get("city")
        district = request.POST.get("district")
        street = request.POST.get("street")
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
        return redirect("/auth/profile/")

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
