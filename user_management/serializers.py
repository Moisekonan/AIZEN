from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TodoUserProfile

class TodoUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoUserProfile
        fields = ('phone',)

class UserSerializer(serializers.ModelSerializer):
    
    profile = TodoUserProfileSerializer(source='todouserprofile', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile')