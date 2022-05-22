from xml.etree.ElementInclude import include
from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r"register", views.UserViewSet)
router.register(r"user", views.CitizenViewSet)
router.register(r"admin", views.AdminViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
