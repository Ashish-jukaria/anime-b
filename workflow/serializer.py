from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    print('hello')
    password=serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username','password']

    def create(self,validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        print(user)
        user.save()
        return user
    
class AniListSearchSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=255, required=True)
    genre = serializers.CharField(max_length=255, required=False)

class PrefrenceSerializer(serializers.Serializer):
    prefrence = serializers.ListField(
        child=serializers.CharField(max_length=255),
        required=True
    )
