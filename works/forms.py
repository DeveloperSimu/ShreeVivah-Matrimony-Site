from django import forms
from .models import Firstlook, MehendiDesign, Testimonial
import re


class FirstlookForm(forms.ModelForm):
    image = forms.ImageField(max_length=None)

    class Meta:
        model = Firstlook
        fields = ["title", "description", "image"]
        labels = {
            "title": "Couple or story title",
            "description": "Their story",
            "image": "Story photo",
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Rohan & Priya",
                "maxlength": 200,
            }),
            "description": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Share the story behind their first meeting...",
            }),
        }

    def clean_title(self):
        title = re.sub(r"\s*&\s*", " ❤️ ", self.cleaned_data["title"]).strip()
        if len(title) > 200:
            raise forms.ValidationError(
                "The title is too long after replacing '&' with a heart."
            )
        return title


class MehendiDesignForm(forms.ModelForm):
    image = forms.ImageField(max_length=None)

    class Meta:
        model = MehendiDesign
        fields = ["title", "category", "description", "image"]
        labels = {
            "title": "Design name",
            "category": "Mehendi style",
            "description": "About this design",
            "image": "Design photo",
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "e.g. Floral bridal trail",
                "maxlength": 120,
            }),
            "category": forms.Select(),
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Share a few details about the design (optional)",
            }),
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'tagline', 'quote', 'rating', 'avatar']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Couple Name (e.g. Amit & Neha)'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. Married in 2023'}),
            'quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your testimonial...'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5, 'placeholder': '1-5'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
