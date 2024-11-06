from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, RegisterViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register', RegisterViewSet.as_view(), name='register')

]