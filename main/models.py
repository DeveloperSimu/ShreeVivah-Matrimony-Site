from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=10,
        choices=(("male", "Male"), ("female", "Female")),
        default="male"
    )

    def __str__(self):
        return f"{self.user.username} - {self.gender}"

class GroomProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(max_length=120, blank=True, null=True, unique=True)
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=160, blank=True)
    about = models.TextField()
    expectations = models.TextField(blank=True)
    family = models.TextField(blank=True)
    photo = models.ImageField(upload_to="groom_photos/", blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True)
    is_sample = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ("-is_featured", "name")

    @property
    def gender(self):
        return "groom"

    def __str__(self):
        return self.name

class BrideProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(max_length=120, blank=True, null=True, unique=True)
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=160, blank=True)
    about = models.TextField()
    expectations = models.TextField(blank=True)
    family = models.TextField(blank=True)
    photo = models.ImageField(upload_to="bride_photos/", blank=True, null=True)
    image_path = models.CharField(max_length=255, blank=True)
    is_sample = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ("-is_featured", "name")

    @property
    def gender(self):
        return "bride"

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]
