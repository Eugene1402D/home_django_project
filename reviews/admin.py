from django.contrib import admin
from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "review_text", "rating", "created_at")
    list_display_links = ("id", "user_name")
    search_fields = ("user_name", "created_at")
    list_filter = ("created_at",)


admin.site.register(Review, ReviewAdmin)
