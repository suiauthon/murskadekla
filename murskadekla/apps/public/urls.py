from django.urls import path

from . import views

app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),
    path("our_story", views.our_story, name="our_story"),
    path("products", views.products, name="products"),
    path("drinks", views.drinks, name="drinks"),
    path("contact", views.contact, name="contact"),
    path("contact", views.contact, name="privacy_policy"),
    path("contact", views.contact, name="terms_and_conditions"),
]
