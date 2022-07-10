from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from api import serializers

from api.models import (
    CV,
    Admin,
    CertificateDocument,
    Citizen,
    Document,
    EducationDocument,
    NinInfo,
    ProfessionalDocument,
    User,
)
from api.serializers import (
    AdminSerializers,
    CVSerializer,
    CertificateDocumentSeriaizer,
    CitizenSerializers,
    DocumentSerializers,
    EducationDocumentSerializers,
    NinInfoSerializers,
    ProfessionalDocumentSerializer,
    UserSerializers,
)


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


class UserViewSet(viewsets.ModelViewSet):
    """The API endpoint that performs CURD operations on the User Model"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = []

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid:
            nin_info = NinInfo.objects.get(citizen__user=request.user)
            serializer = self.get_serializer(nin_info)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid:
            document_instance = get_object_or_404(
                Document, nin_info__citizen__user=request.user
            )
            serializer = self.get_serializer(document_instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class EducationDocumentViewSet(viewsets.ModelViewSet):
    queryset = EducationDocument.objects.all()
    serializer_class = EducationDocumentSerializers
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid:
            education_instance = get_object_or_404(
                EducationDocument, certificate__nin_info__citizen__user=request.user
            )
            serializer = self.get_serializer(education_instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid:
            cv_instance = get_object_or_404(
                CV, cv__nin_info__citizen__user=request.user
            )
            serializer = self.get_serializer(cv_instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProfessionalDocumentViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalDocument.objects.all()
    serializer_class = ProfessionalDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid:
            professional_instance = get_object_or_404(
                ProfessionalDocument, document__nin_info__citizen__user=request.user
            )
            serializer = self.get_serializer(professional_instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class CertificateDocumentViewSet(viewsets.ModelViewSet):
    queryset = CertificateDocument.objects.all()
    serializer_class = CertificateDocumentSeriaizer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        print(request)
        if serializer.is_valid:
            certificate_instance = get_object_or_404(
                CertificateDocument, certificate__nin_info__citizen__user=request.user
            )
            serializer = self.get_serializer(certificate_instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
