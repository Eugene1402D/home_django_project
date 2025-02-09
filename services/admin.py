from django.contrib import admin
from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "price", "description")
    list_display_links = ("id", "name")
    search_fields = ("name", "price")
    list_filter = ("name",)


admin.site.register(Service, ServiceAdmin)
