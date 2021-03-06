from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r"register", views.UserViewSet)
router.register(r"citizen", views.CitizenViewSet)
router.register(r"admin", views.AdminViewSet)
router.register(r"nininfo", views.NinInfoViewSet)
router.register(r"document", views.DocumentViewSet)
router.register(r"education-document", views.EducationDocumentViewSet)
router.register(r"professional-document", views.ProfessionalDocumentViewSet)
router.register(r"certificate", views.CertificateDocumentViewSet)
router.register(r"cv", views.CVViewSet)
router.register(r"update-nininfo", views.UpdateNinInfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", views.LogoutView.as_view(), name="auth_logout"),
    path("patner-access/", views.PatnerAccessView.as_view(), name="patner_access"),
    path("update-request/", views.UpdateRequestView.as_view(), name="update_request"),
]
