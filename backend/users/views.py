from django.contrib.auth.models import User
from .serializer import UserSerializer, RegisterUserSerializer
from rest_framework import permissions, viewsets, generics  
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class  = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]

# Create your views here.
