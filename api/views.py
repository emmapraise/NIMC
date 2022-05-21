from django.shortcuts import render
from rest_framework import viewsets

from api.models import User
from api.serializers import UserSerializers

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """The API endpoint that performs CURD operations on the User Model"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
