from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("loyalty/categories/", views.list_category, name="categories"),
    path("loyalty/new_category/", views.new_category, name="new category"),
    path(
        "loyalty/delete_category/<int:id>",
        views.delete_category,
        name="delete category",
    ),
    path(
        "loyalty/update_category/<int:id>",
        views.update_category,
        name="update category",
    ),
    path("loyalty/categories/<int:id>", views.list_product, name="products"),
    path(
        "loyalty/categories/<int:id>/products", views.new_product, name="new products"
    ),
]
