from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django_filters import rest_framework as filters



class AutorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('city',)
    # filter_backends = (filters.DjangoRangeFilter,)
    # filterset_fields = ('birthday',)
