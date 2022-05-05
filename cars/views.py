from django.shortcuts import redirect, render

from cars.forms import CarsForm
from cars.models import Cars


def home(request):
    data = {}
    data["cars"] = Cars.objects.all()
    return render(request, "index.html", data)


def form(request):
    data = {}
    data["form"] = CarsForm()
    return render(request, "form.html", data)


def create(request):
    form = CarsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")


def view(request, pk):
    data = {}
    data["cars"] = Cars.objects.get(pk=pk)
    return render(request, "view.html", data)


def edit(request, pk):
    data = {}
    data["cars"] = Cars.objects.get(pk=pk)
    data["form"] = CarsForm(instance=data["cars"])
    return render(request, "form.html", data)


def update(request, pk):
    data = {}
    data["cars"] = Cars.objects.get(pk=pk)
    form = CarsForm(request.POST or None, instance=data["cars"])
    if form.is_valid():
        form.save()
        return redirect("home")


def delete(request, pk):
    cars = Cars.objects.get(pk=pk)
    cars.delete()
    return redirect("home")
