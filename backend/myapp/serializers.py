from rest_framework import serializers
from .models import Login, Profile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Login.objects.create(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=255, write_only=True)
