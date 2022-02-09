from .models import Daybook_type
from rest_framework import serializers

class Daybook_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daybook_type
        fields = ( 'name')
