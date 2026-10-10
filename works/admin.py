from django.contrib import admin
from .models import Firstlook, MehendiCategory, MehendiDesign

@admin.register(Firstlook)
class FirstlookAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_path', 'image')
    ordering = ('title',)
    search_fields = ('title', 'description')


@admin.register(MehendiCategory)
class MehendiCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(MehendiDesign)
class MehendiDesignAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "submitted_by", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "description", "category__name")
    ordering = ("-created_at", "-pk")
