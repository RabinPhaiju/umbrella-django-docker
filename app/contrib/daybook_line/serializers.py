from .models import Daybook_line
from rest_framework import serializers

class Daybook_lineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daybook_line
        fields = ( 'partner','total')
