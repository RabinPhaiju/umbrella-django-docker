from django.db import models

class Daybook_type(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name} -{self.created.strftime('%d/%m/%Y')}"
