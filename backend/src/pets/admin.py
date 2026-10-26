
from django.contrib import admin

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "species", "owner", "created_at")
    list_filter = ("species", "created_at")
    search_fields = ("name", "breed", "owner__username")
    list_select_related = ("owner",)
