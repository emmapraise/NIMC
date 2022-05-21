from rest_framework import serializers
from NIMC.helpers.nin import generateNin
from api.models import *


class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    nin = serializers.CharField(read_only=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        exclude = [
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "last_login",
            "groups",
            "user_permissions",
        ]

    def create(self, validated_data):
        """Create User"""
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        phone = validated_data["phone"]
        email = validated_data["email"]
        nin = generateNin(10)
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            nin=nin,
            email=email,
            username=email,
            avatar=validated_data["avatar"],
            gender=validated_data["gender"],
            password=validated_data["password"],
        )
        user.save()
        return user
