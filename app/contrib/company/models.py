from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=220)
    image = models.CharField(max_length=120,default='default.jpg')
    verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Company: {self.name} & Address: {self.address}-{self.created.strftime('%d/%m/%Y')}"
