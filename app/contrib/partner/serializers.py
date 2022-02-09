from .models import Partner
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ( 'user', 'company')
