from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet, RegisterViewSet
from canchas.views import CanchaViewSet, LugarViewSet
from reservas.views import ReservasViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'canchas', CanchaViewSet)
router.register(r'lugar', LugarViewSet)
router.register(r'reservas', ReservasViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', RegisterViewSet.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
