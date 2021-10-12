from django.conf import settings
from django.conf.urls.static import static

from .router import router

from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('user/', include('user.urls')),
    path('router/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
