from rest_framework import serializers
from profile_api import models


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )

        return user
