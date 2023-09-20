from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name='home'),
    path("category/", views.list_category, name='category'),
    path("new_category/", views.new_category, name='new category'),
]