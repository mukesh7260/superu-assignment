from rest_framework import serializers 
from superapp.models import Profile 


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ['name','email','bio','profile_picture'] 

class UserProfileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=25) 

