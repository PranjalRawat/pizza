from django.db import models
from django.urls import reverse

# Create your models here.
class Pizza(models.Model):
    REGULAR = 'regular'
    SQUARE  = 'square'

    Pizza_type = [
        (REGULAR, 'regular'),
        (SQUARE, 'square'),
    ]
    Pizza_type = models.CharField(
        max_length=18,
        choices=Pizza_type,
        default=REGULAR,
    )
    category  = models.CharField(max_length=140)
    topping   = models.CharField(max_length=140)
    name      = models.CharField(max_length=140)

    def get_absolute_url(self):
        return reverse("product:detail" ,kwargs={"pk":self.pk})