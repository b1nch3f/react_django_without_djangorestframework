from django.shortcuts import render
from django.template import Template, Context


def index(request):
    data = {"name": "maxx"}
    return render(request, "app/index.html", data)

def link1(request):
    return render(request, "app/link1.html")

def link2(request):
    return render(request, "app/link2.html")
