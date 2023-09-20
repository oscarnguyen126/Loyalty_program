from django.shortcuts import render, redirect
from .models import Category, Product
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def list_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html',  {'cats': cats})


def new_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if len(Category.objects.filter(name=name)) < 1:
            cat = Category(name=name)
            cat.save()
            return redirect('/loyalty/category')
    
    return render(request, 'add_category.html')
