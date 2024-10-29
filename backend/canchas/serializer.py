from rest_framework import serializer
from .models import Canchas
from django.contrib.auth.models import User


class canchaSerializer(serializer.ModelSerializer):
    user = 