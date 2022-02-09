from django.db import models
from contrib.company.models import Company
from contrib.user.models import UserProfile
from contrib.daybook_line.models import Daybook_line

class Daybook(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    daybook_line = models.ForeignKey(Daybook_line, on_delete=models.CASCADE)
    month = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"month: {self.month} & company: {self.company} & name: {self.name}-{self.created.strftime('%d/%m/%Y')}"
