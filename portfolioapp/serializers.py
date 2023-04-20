from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class LoginSerializer(TokenObtainPairSerializer):
    ''' Login Serializer '''
    username = serializers.CharField(
        max_length=255, allow_blank=False)
    password = serializers.CharField(
        max_length=40, allow_blank=False)

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['id'] = self.user.pk
        return data


class SignUpSerializer(serializers.ModelSerializer):
    ''' Sign Up Serializer '''
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"is_staff":{"required": False}, "is_active":{"required": False}, "username":{"required": False},"email":{"required": False}, "password":{"write_only": True, "required": False}}

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.name = validated_data.get("name", instance.name)
        instance.home_address = validated_data.get("home_address", instance.home_address)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.save()
        return instance
    
