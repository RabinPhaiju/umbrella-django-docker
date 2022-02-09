from .models import Daybook
from rest_framework import serializers

class DaybookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daybook
        fields = ( 'name','user', 'company','month')
