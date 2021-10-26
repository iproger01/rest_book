from rest_framework import viewsets, permissions
from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer