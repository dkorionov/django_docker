from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Custom user registration serializer
    """
    re_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'phone', 'password', 're_password', ]

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    phone=validated_data['phone'], )

        password = validated_data['password']
        re_password = validated_data['re_password']
        if password != re_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user

    extra_kwargs = {
        'password': {'write_only': True},
    }
