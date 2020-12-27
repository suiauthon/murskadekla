from django.shortcuts import render
import datetime


def index(request):
    print(request.user)
    args = {}
    args["YEAR"] = datetime.datetime.now().year
    return render(request, "index.html", args)


def our_story(request):
    return render(request, "our_story.html")


def products(request):
    return render(request, "products.html")


def drinks(request):
    return render(request, "drinks.html")


def contact(request):
    return render(request, "contact.html")
