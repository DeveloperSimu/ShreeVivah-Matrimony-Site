from django import forms
from .models import GroomProfile, BrideProfile, Comment


class ProfileDetailsForm(forms.ModelForm):
    required_profile_fields = (
        "name",
        "profession",
        "location",
        "about",
        "expectations",
        "family",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Full Name"
        self.fields["about"].label = "About Myself"
        self.fields["family"].label = "Family Details"
        self.fields["photo"].label = "Profile Photo"
        for field_name in self.required_profile_fields:
            self.fields[field_name].required = True
        self.fields["photo"].required = False
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "profile-form-control"
            field.widget.attrs["placeholder"] = field.label
        self.fields["about"].widget = forms.Textarea(
            attrs={"class": "profile-form-control", "rows": 4, "placeholder": "About"}
        )
        self.fields["expectations"].widget = forms.Textarea(
            attrs={
                "class": "profile-form-control",
                "rows": 4,
                "placeholder": "Expectations",
            }
        )
        self.fields["family"].widget = forms.Textarea(
            attrs={
                "class": "profile-form-control",
                "rows": 4,
                "placeholder": "Family details",
            }
        )


class GroomForm(ProfileDetailsForm):
    class Meta:
        model = GroomProfile
        fields = [
            "name",
            "profession",
            "location",
            "about",
            "expectations",
            "family",
            "photo",
        ]


class BrideForm(ProfileDetailsForm):
    class Meta:
        model = BrideProfile
        fields = [
            "name",
            "profession",
            "location",
            "about",
            "expectations",
            "family",
            "photo",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
