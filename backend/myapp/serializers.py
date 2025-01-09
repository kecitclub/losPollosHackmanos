from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Login, Profile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password before saving
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return Login.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Hash password if provided
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        return super().update(instance, validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=255, write_only=True)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username']