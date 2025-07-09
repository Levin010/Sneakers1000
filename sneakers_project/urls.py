from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from sneakers_project.sneakers.views import debug_media

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", (include("djoser.urls"))),
    path("api/v1/", (include("djoser.urls.authtoken"))),
    path("api/v1/", include("sneakers_project.sneakers.urls")),
    path("api/v1/", include("sneakers_project.order.urls")),
    path("debug/media/", debug_media, name="debug_media"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
