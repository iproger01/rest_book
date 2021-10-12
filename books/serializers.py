from rest_framework import serializers
from .models import *


class AutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ('id', 'name', 'surename', 'fathername', 'city', 'birthday')

