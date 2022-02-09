from django.db import models
from contrib.partner.models import Partner

class Daybook_line(models.Model):
    id = models.AutoField(primary_key=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    # type
    # order
    date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"partner: {self.partner} & total: {self.total}-{self.created.strftime('%d/%m/%Y')}"
