# from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import Admin, Citizen, NinInfo, User
from api.serializers import (
    AdminSerializers,
    CitizenSerializers,
    NinInfoSerializers,
    UserSerializers,
)

# User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            user = get_object_or_404(User, username=request.data["username"])
            serializer.is_valid(raise_exception=True)
            status_code = status.HTTP_200_OK
            response = {
                "data": {
                    "tokens": serializer.validated_data,
                    "user": UserSerializers(user).data,
                },
                "status": "success",
                "message": "User successfully authenticated",
            }
        except User.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                "data": {},
                "status": "failure",
                "message": "User account not found",
            }
        except TokenError:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                "data": {},
                "status": "failure",
                "message": "Token is invalid or expired",
            }

        return Response(data=response, status=status_code)


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """The API endpoint that performs CURD operations on the User Model"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializers
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializers
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class NinInfoViewSet(viewsets.ModelViewSet):
    queryset = NinInfo.objects.all()
    serializer_class = NinInfoSerializers
    permission_classes = [permissions.IsAuthenticated]
