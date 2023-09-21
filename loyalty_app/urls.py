from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("categories/", views.list_category, name="categories"),
    path("new_category/", views.new_category, name="new category"),
    path("delete_category/<int:id>", views.delete_category, name="delete category"),
    path("update_category/<int:id>", views.update_category, name="update category"),
    path("categories/<int:id>", views.list_product, name="products"),
]
