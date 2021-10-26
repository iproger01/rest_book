from rest_framework import serializers, status
from rest_framework.response import Response

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'post_agreement', 'first_name', 'last_name', 'patronymic', 'is_active', 'is_superuser',
                  'inn', 'bank_acaunt', 'phone', 'address')
