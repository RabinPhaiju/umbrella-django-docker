from django.db import models
from contrib.product.models import Product
from contrib.partner.models import Partner
# from contrib.

class Daybook_order(models.Model):
    id = models.AutoField(primary_key=True)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    s_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    name= models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"s_price: {self.s_price} -{self.created.strftime('%d/%m/%Y')}"
