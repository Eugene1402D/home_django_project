from django.contrib import admin
from .models import *


class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "start_date", "description")
    list_display_links = ("id", "title")
    search_fields = ("title", "start_date")
    list_filter = ("start_date",)

admin.site.register(SpecialOffer, SpecialOfferAdmin)
admin.site.register(GalleryImage)