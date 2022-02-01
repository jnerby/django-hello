from curses.ascii import HT
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hello/index.html")

def jen(request):
    return HttpResponse("Hello, Jen!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")