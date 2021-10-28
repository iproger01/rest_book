from rest_framework import serializers, status
from rest_framework.response import Response
from .service import send_email

from .models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        user = User(**validated_data)
        password = validated_data.get('password',  None)
        user.set_password(password)

        send_email.delay()
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'post_agreement', 'first_name', 'last_name', 'patronymic', 'is_active', 'is_superuser',
                  'inn', 'bank_acaunt', 'phone', 'address')
