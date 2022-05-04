from dataclasses import fields

from django.forms import ModelForm

from cars.models import Cars


class CarsForm(ModelForm):
    class Meta:
        model = Cars
        fields = ["model", "brand", "year"]
