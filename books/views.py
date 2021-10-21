from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 12

class AutorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        autors = Autor.objects.all()
        serializer = AutorSerializer(autors, many=True)
        return Response(serializer.data)


class BooksView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = LargeResultsSetPagination

    # def get(self, request):
    #     books = Books.objects.all()
    #     serializer = BookSerializer(books, many=True)
    #     return Response(serializer.data)