# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from social_network_app.helpers import CustomExceptionHandler
from social_network_app.status_code import password_does_not_match

User = get_user_model()



# Serializer for user registration
class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'password2')

    def validate_email(self, value):
        return value.lower()
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise CustomExceptionHandler(password_does_not_match)
        return attrs

    def create(self, validated_data):

        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user