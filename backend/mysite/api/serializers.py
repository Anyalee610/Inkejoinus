from rest_framework import serializers
from .models import JoinUs

class JoinUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUs
        fields = ['id', 'firstname', 'lastname', 'email','message','published_date']
        
    def validate_email(self, value):
        """
        Check if the email already exists in the database.
        """
        if JoinUs.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value