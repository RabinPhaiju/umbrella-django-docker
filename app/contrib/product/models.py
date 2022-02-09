from pydoc import describe
from unicodedata import category
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    photo = models.CharField(max_length=120, default="default.png")
    quantity = models.IntegerField(default=0)
    min_quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    code = models.CharField(max_length=120, default="")
    p_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.CharField(max_length=120, default="")
    sub_category = models.CharField(max_length=120, default="")
    sub_category_type = models.CharField(max_length=120, default="")
    warrenty = models.CharField(max_length=120, default="")
    made = models.CharField(max_length=120, default="")
    description = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name} & quantity: {self.quantity} & price: {self.price}-{self.created.strftime('%d/%m/%Y')}"

