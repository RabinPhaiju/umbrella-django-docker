from django.db import models
from contrib.company.models import Company

class Daybook(models.Model):
    month = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=120)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"month: {self.month} & company: {self.company.name} & name: {self.name}-{self.created.strftime('%d/%m/%Y')}"
