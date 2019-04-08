from django.contrib.auth import get_user_model

from rest_framework import serializers

from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "password", "is_superuser","roles")
