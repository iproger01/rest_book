from rest_framework import routers
from books.viewsets import *
from user.viewsets import *

router = routers.DefaultRouter()
router.register('autors', AutorViewSet)
router.register('users', UserViewSet)