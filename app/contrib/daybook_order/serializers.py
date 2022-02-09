from .models import Daybook_order
from rest_framework import serializers

class Daybook_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daybook_order
        fields = ( 's_price')
