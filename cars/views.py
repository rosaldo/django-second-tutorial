from django.shortcuts import redirect, render

from cars.forms import CarsForm


def home(request):
    return render(request, "index.html")


def form(request):
    data = {}
    data["form"] = CarsForm()
    return render(request, "form.html", data)


def create(request):
    form = CarsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
