from django.urls import path, re_path

from . import views

app_name = "plantatree"
urlpatterns = [
    path("plant_a_tree", views.plant_a_tree, name="plant_a_tree"),
]