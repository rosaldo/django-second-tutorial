from django.shortcuts import render

from cars.forms import CarsForm


def home(request):
    return render(request, "index.html")


def form(request):
    data = {}
    data["form"] = CarsForm()
    return render(request, "form.html", data)
