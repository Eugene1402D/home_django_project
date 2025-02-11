from django.contrib import admin
from .models import *


# класс используется для настройки отображения модели SpecialOffer в административной панели Django
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "start_date", "description")  # Указывает, какие поля модели будут отображаться в виде списка в административной панели
    list_display_links = ("id", "title")  # Указывает, какие поля будут ссылками, ведущими к деталям объекта
    search_fields = ("title", "start_date")  # Указывает, по каким полям можно выполнять поиск в административной панели
    list_filter = ("start_date",)  # Указывает, по каким полям можно фильтровать список объектов в административной панели

"""Регистрирует модель SpecialOffer и настраивает её представление с помощью класса SpecialOfferAdmin
в административной панели Django"""
admin.site.register(SpecialOffer, SpecialOfferAdmin)
admin.site.register(GalleryImage)