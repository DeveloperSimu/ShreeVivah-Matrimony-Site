from django.contrib import admin
from django.db import models
from .models import BrideProfile, GroomProfile


@admin.register(GroomProfile)
class GroomProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {models.ImageField: {"required": False}}
    list_display = ("name", "profession", "location", "is_sample", "is_featured")
    list_filter = ("is_sample", "is_featured")
    list_editable = ("is_featured",)
    search_fields = ("name", "profession", "location", "about")
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {"fields": ("name", "slug", "user", "is_sample", "is_featured")}),
        ("Profile details", {"fields": ("profession", "location", "about", "expectations", "family")}),
        ("Profile photo", {"fields": ("photo", "image_path")}),
    )


@admin.register(BrideProfile)
class BrideProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {models.ImageField: {"required": False}}
    list_display = ("name", "profession", "location", "is_sample", "is_featured")
    list_filter = ("is_sample", "is_featured")
    list_editable = ("is_featured",)
    search_fields = ("name", "profession", "location", "about")
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (None, {"fields": ("name", "slug", "user", "is_sample", "is_featured")}),
        ("Profile details", {"fields": ("profession", "location", "about", "expectations", "family")}),
        ("Profile photo", {"fields": ("photo", "image_path")}),
    )
