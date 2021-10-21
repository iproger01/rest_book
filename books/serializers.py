from rest_framework import serializers, status
from rest_framework.response import Response
from .models import *


class AutorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        autor = Autor(**validated_data)

        autor.save()
        return autor

        #return Response(data=validated_data, status=status.HTTP_200_OK)

        # Использование метода модели
        # autor = Autor.objects.create_autor(name=validated_data['name'], surename=validated_data['surename'], fathername=validated_data['fathername'], city=validated_data['city'], birthday=validated_data['birthday'])
        # return autor
    # def update(self, validated_data, instance):


    class Meta:
        model = Autor
        fields = ('name', 'surename', 'birthday')


class BookSerializer(serializers.ModelSerializer):

    autor_relative = AutorSerializer(read_only=True )

    class Meta:
        model = Books
        fields = '__all__'

