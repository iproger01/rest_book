from django.conf import settings
from django.conf.urls.static import static

from .router import router

from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('user/', include('user.urls')),
    path('router/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
