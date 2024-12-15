from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields= ['username','email', 'first_name', 'last_name', 'is_superuser']

class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required= True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only= True, required = True, validators=[validate_password])
    password2 = serializers.CharField(write_only= True, required = True)
    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def create(self, validated_data):
        user= User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
            password= validated_data['password'],
        )
        return user
