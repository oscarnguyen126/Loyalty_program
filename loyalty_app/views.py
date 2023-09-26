from django.shortcuts import render, redirect
from .models import Category, Product
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, "home.html")


def list_product(request, id):
    try:
        cat = Category.objects.get(id=id)
        products = Product.objects.filter(category_id=id)
        return render(
            request, "category_product.html", {"products": products, "cat": cat}
        )
    except:
        return redirect("home")


def new_product(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        expired_time = request.POST.get("expired_time")
        category_id = Category.objects.get(id=id)
        product = Product(
            name=name,
            description=description,
            price=price,
            expired_time=expired_time,
            category_id=category_id,
        )
        product.save()
        return redirect("/loyalty/categories")

    return render(request, "add_product.html", {"id": id})


def list_category(request):
    cats = Category.objects.all()
    return render(request, "category.html", {"cats": cats})


def new_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if len(Category.objects.filter(name=name)) < 1:
            cat = Category(name=name)
            cat.save()
            return redirect("/loyalty/categories")

    return render(request, "add_category.html")


def delete_category(request, id):
    cat = get_object_or_404(Category, id=id)
    cat.delete()
    return redirect("/loyalty/categories")


def update_category(request, id):
    cat = get_object_or_404(Category, id=id)
    name = request.POST.get("name")
    cat.name = name
    cat.save()
    return redirect("/loyalty/categories")


def terms_and_cons(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")