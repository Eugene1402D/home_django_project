from django.contrib import admin
from .models import *


class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "description", "price")
    list_display_links = ("id", "name")
    search_fields = ("name", "room_type")
    list_filter = ("price",)


admin.site.register(Room, RoomAdmin)
