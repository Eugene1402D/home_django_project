from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("info/", include("info.urls")),
    path("services/", include("services.urls")),
    path("rooms/", include("rooms.urls")),
    path("accounts/", include("accounts.urls")),
    path('booking/', include('accounts.urls')),
    path("reviews/", include("reviews.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path("__debug__/", include(debug_toolbar.urls)),
                  ] + urlpatterns
