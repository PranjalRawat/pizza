from django import forms

from .models import Pizza

class PizzaModelForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = [
            "Pizza_type",
            "category",
            "topping",
            "name",
        ]

    