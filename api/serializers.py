from rest_framework import serializers

# from NIMC.helpers.face_reg import extract_feature
from NIMC.helpers.nin import generateNin
from api.models import *


class UserSerializers(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    nin = serializers.CharField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_citizen = serializers.BooleanField(read_only=True)
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


class CitizenSerializers(serializers.ModelSerializer):

    user = UserSerializers()

    class Meta:
        model = Citizen
        fields = "__all__"

    def create(self, validated_data):
        user = UserSerializers.create(self, validated_data["user"])
        user.is_citizen = True
        user.save()

        citizen = Citizen.objects.create(user=user)
        return citizen


class AdminSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        model = Admin
        exclude = ["create_at", "update_at"]

    def create(self, validated_data):
        user = UserSerializers.create(self, validated_data["user"])
        user.is_admin = True
        user.save()

        if "user" in validated_data:
            del validated_data["user"]
        new_admin = validated_data
        new_admin["user"] = user
        admin = Admin.objects.create(**new_admin)
        return admin


class NinInfoSerializers(serializers.ModelSerializer):
    """A serializer for all actions on Nin Info"""

    citizen = CitizenSerializers()

    class Meta:
        model = NinInfo
        exclude = ["create_at", "update_at"]

    def create(self, validated_data):
        citizen = CitizenSerializers.create(self, validated_data["citizen"])
        # avatar = validated_data["citizen"]["user"]["avatar"]
        # if avatar is not None:
        #     EncodedImage.objects.create(
        #         citizen=citizen, encodings=extract_feature(avatar)
        #     )
        if "citizen" in validated_data:
            del validated_data["citizen"]
        new_ninifo = validated_data
        new_ninifo["citizen"] = citizen
        nin_info = NinInfo.objects.create(**new_ninifo)
        return nin_info


class DocumentSerializers(serializers.ModelSerializer):
    """Serializer for all actions on Documents"""

    class Meta:
        model = Document
        exclude = ["create_at", "update_at"]


class EducationDocumentSerializers(serializers.ModelSerializer):
    """Serializer for all action on Education Documents"""

    certificate = DocumentSerializers()
    transcript = DocumentSerializers()

    class Meta:
        model = EducationDocument
        exclude = ["create_at", "update_at"]

        # def create(self, validated_data):
