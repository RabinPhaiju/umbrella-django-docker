from django.db import models
from contrib.partner.models import Partner
from contrib.daybook_type.models import Daybook_type
from contrib.daybook.models import Daybook

class Daybook_line(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    daybook = models.ForeignKey(Daybook, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.DO_NOTHING)
    daybook_type = models.ForeignKey(Daybook_type,on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"partner: {self.partner} & total: {self.total}-{self.created.strftime('%d/%m/%Y')}"


# order ma chai day_book line rakhne