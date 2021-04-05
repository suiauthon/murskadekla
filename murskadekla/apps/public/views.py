import bleach
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.mail import send_mail, get_connection, EmailMessage

from .forms import ContactForm
from murskadekla import settings

import datetime

def index(request):
    print(request.user)
    args = {}
    args["YEAR"] = datetime.datetime.now().year

    response = render(request, "index.html", args)
    return response


def our_story(request):
    args = {}
    args["YEAR"] = datetime.datetime.now().year
    return render(request, "our_story.html", args)


def products(request):
    return render(request, "products.html")


def drinks(request):
    return render(request, "drinks.html")


def contact(request: HttpRequest) -> HttpResponse:
    args = {}
    args["YEAR"] = datetime.datetime.now().year

    if request.method == "GET":
        form = ContactForm()
        args["form"] = form
        response = render(request, "contact.html", args)
        response.set_cookie("contactToken", value='allow')
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() and request.COOKIES["contactToken"] =='allow':
            connections = getattr(settings, 'EMAIL_CONNECTIONS')
            options = connections['contact']
            print(options['username'])
            connection = get_connection(**options)
            name = bleach.clean(form.cleaned_data["name"])
            email = bleach.clean(form.cleaned_data["email"])
            subject = bleach.clean(form.cleaned_data["subject"])
            message = bleach.clean(form.cleaned_data["message"])
            msg = EmailMessage(f"[nesto] {subject}",
                               message,
                               from_email=options['username'],
                               to=[email],
                               connection=connection)
            msg.send()
            form.save()
            args["form"] = ContactForm()
            args["success"] = True
            args["anchor"] = "contact-form"
            response = render(request, "contact.html", args)
            response.set_cookie("contactToken", value='disable')
        else:
            args["form"] = form
            args["anchor"] = "contact-form"
            response = render(request, "contact.html", args)
    else:
        raise NotImplementedError

    return response
