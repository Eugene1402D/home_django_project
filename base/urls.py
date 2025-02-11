from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("special_offers/", views.special_offers, name="special_offers"),
    path("gallery/", views.gallery_list, name="gallery_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
