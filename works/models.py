from pathlib import Path
import re
from uuid import uuid4

from django.conf import settings
from django.db import models


def firstlook_image_upload_to(instance, filename):
    extension = Path(filename).suffix.lower()
    if extension not in {".jpg", ".jpeg", ".png", ".gif", ".webp"}:
        extension = ".img"
    return f"firstlook/{uuid4().hex}{extension}"


def mehendi_image_upload_to(instance, filename):
    extension = Path(filename).suffix.lower()
    if extension not in {".jpg", ".jpeg", ".png", ".gif", ".webp"}:
        extension = ".img"
    return f"mehendi/{uuid4().hex}{extension}"


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    quote = models.TextField()
    rating = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to='user/', default='user/default.jpg')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Firstlook(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=firstlook_image_upload_to, blank=True)
    image_path = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Firstlove story"
        verbose_name_plural = "Firstlove stories"
    
    def save(self, *args, **kwargs):
        self.title = re.sub(r"\s*&\s*", " ❤️ ", self.title).strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class MehendiCategory(models.Model):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Mehendi type"
        verbose_name_plural = "Mehendi types"

    def __str__(self):
        return self.name


class MehendiDesign(models.Model):
    category = models.ForeignKey(
        MehendiCategory,
        on_delete=models.PROTECT,
        related_name="designs",
    )
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=mehendi_image_upload_to, blank=True)
    image_path = models.CharField(max_length=255, blank=True)
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="mehendi_designs",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at", "-pk")
        verbose_name = "Mehendi design"
        verbose_name_plural = "Mehendi designs"

    def __str__(self):
        return self.title
