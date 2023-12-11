from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, date

# Create your views here.

def show_html(request):
    contexto = {
        "nombre": "Welcome",
    }
    return render(request, template_name="index.html", context=contexto)

def about_me(request):
    contexto = {

    }
    return render(request, template_name="AppCoder/about_me.html", context=contexto)