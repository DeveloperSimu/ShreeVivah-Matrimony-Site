from io import BytesIO
from tempfile import TemporaryDirectory
from types import SimpleNamespace

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse
from PIL import Image

from .models import BrideProfile, GroomProfile
from profiles.profile_data import FEATURED_BRIDES, FEATURED_GROOMS


class HomepagePreferenceSectionTests(TestCase):
    def test_preference_cards_keep_their_existing_profile_routes(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Browse by")
        self.assertContains(response, "preference")
        self.assertContains(
            response,
            f'href="{reverse("groom")}" class="gender-btn">Explore grooms',
        )
        self.assertContains(
            response,
            f'href="{reverse("bride")}" class="gender-btn">Explore brides',
        )


class ContactPageTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="contactviewer",
            password="test-password",
        )
        self.client.force_login(user)

    def test_contact_page_keeps_contact_channels_and_form(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/static/main/css/contact.css?v=2")
        self.assertContains(response, 'href="mailto:support@shreevivah.com"')
        self.assertContains(response, 'href="tel:+919876543210"')
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="phone"')
        self.assertContains(response, 'name="message"')
        self.assertContains(response, 'name="csrfmiddlewaretoken"')


class SuccessStoriesTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="storyviewer",
            password="StoryViewer!4821",
        )
        self.client.force_login(user)

    def test_success_stories_render_cards_and_photo_details_dialog(self):
        response = self.client.get("/success_stories/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.count(b'class="story-card"'), 12)
        self.assertContains(response, 'class="story-dialog"')
        self.assertContains(response, 'class="story-dialog-photo"')
        self.assertContains(
            response,
            "/static/main/css/success_stories.css?v=5",
        )
        self.assertContains(response, "Real stories.")
        self.assertContains(response, "12 stories of togetherness")
        self.assertContains(response, "/static/main/js/success_stories.js?v=7")
        self.assertContains(response, "View full story")

    def test_bride_and_groom_pages_show_at_least_ten_cards(self):
        for path in ("/bride/", "/groom/"):
            with self.subTest(path=path):
                response = self.client.get(path)

                self.assertEqual(response.status_code, 200)
                self.assertGreaterEqual(
                    response.content.count(b'class="bride-card'),
                    10,
                )
                self.assertNotContains(response, "Comments")
                self.assertContains(response, "Create Profile")
                self.assertContains(response, "profiles/js/profile-scroll.js?v=1")

    def test_member_can_create_a_complete_profile_from_either_page(self):
        profile_details = {
            "name": "Community Member",
            "profession": "Architect",
            "location": "Kolkata, India",
            "about": "I enjoy designing thoughtful spaces.",
            "expectations": "Looking for a kind and supportive partner.",
            "family": "I come from a close and caring family.",
        }

        for profile_type, model, list_name, detail_name in (
            ("bride", BrideProfile, "bride", "bride_detail"),
            ("groom", GroomProfile, "groom", "groom_detail"),
        ):
            with self.subTest(profile_type=profile_type):
                response = self.client.post(
                    reverse(f"create_{profile_type}"),
                    profile_details,
                )

                self.assertRedirects(response, reverse(list_name))
                profile = model.objects.get(name="Community Member")
                self.assertEqual(profile.profession, "Architect")
                self.assertEqual(profile.location, "Kolkata, India")
                self.assertEqual(profile.about, profile_details["about"])
                self.assertEqual(profile.expectations, profile_details["expectations"])
                self.assertEqual(profile.family, profile_details["family"])

                listing = self.client.get(reverse(list_name))
                self.assertContains(listing, "Community Member")
                self.assertContains(listing, "Architect")
                self.assertContains(listing, "Kolkata, India")
                self.assertContains(
                    listing,
                    reverse(detail_name, args=(profile.pk,)),
                )

                detail = self.client.get(reverse(detail_name, args=(profile.pk,)))
                self.assertContains(detail, "Community Member")
                self.assertContains(detail, "Architect")
                self.assertContains(detail, "Looking for a kind and supportive partner.")
                self.assertContains(detail, "I come from a close and caring family.")

    def test_create_profile_forms_require_all_card_details(self):
        for profile_type in ("bride", "groom"):
            with self.subTest(profile_type=profile_type):
                response = self.client.get(reverse(f"create_{profile_type}"))

                self.assertEqual(response.status_code, 200)
                for field in (
                    "name",
                    "profession",
                    "location",
                    "about",
                    "expectations",
                    "family",
                    "photo",
                ):
                    self.assertIn(field, response.context["form"].fields)

                invalid_response = self.client.post(reverse(f"create_{profile_type}"), {})
                self.assertEqual(invalid_response.status_code, 200)
                self.assertEqual(
                    set(invalid_response.context["form"].errors),
                    {"name", "profession", "location", "about", "expectations", "family"},
                )

    def test_member_profiles_replace_placeholders_without_reducing_card_count(self):
        user = get_user_model().objects.get(username="storyviewer")
        BrideProfile.objects.create(
            user=user,
            name="Member Bride",
            about="Enjoys painting and music.",
        )
        GroomProfile.objects.create(
            user=user,
            name="Member Groom",
            about="Enjoys reading and hiking.",
        )

        for path, member_name in (
            ("/bride/", "Member Bride"),
            ("/groom/", "Member Groom"),
        ):
            with self.subTest(path=path):
                response = self.client.get(path)

                self.assertEqual(response.status_code, 200)
                self.assertGreaterEqual(
                    response.content.count(b'class="bride-card'),
                    10,
                )
                self.assertContains(response, member_name)

    def test_bride_and_groom_pages_include_five_additional_sample_profiles(self):
        for path, featured_profiles in (
            ("/bride/", FEATURED_BRIDES),
            ("/groom/", FEATURED_GROOMS),
        ):
            with self.subTest(path=path):
                response = self.client.get(path)

                self.assertEqual(response.status_code, 200)
                self.assertEqual(
                    response.content.count(b'class="bride-card'),
                    10,
                )
                self.assertContains(response, "Sample profile")
                self.assertContains(response, "View Profile")
                for profile in featured_profiles:
                    self.assertContains(response, profile["name"])
                    self.assertContains(response, profile["profession"])
                    self.assertContains(response, profile["location"])
                    self.assertContains(response, f"/profiles/details/{profile['slug']}/")

    def test_static_profiles_are_managed_in_separate_bride_and_groom_sections(self):
        self.assertEqual(BrideProfile.objects.filter(is_sample=True).count(), 10)
        self.assertEqual(GroomProfile.objects.filter(is_sample=True).count(), 10)
        self.assertEqual(BrideProfile.objects.get(slug="ankita").image_path, "main/images/Ankita.jpeg")
        self.assertEqual(GroomProfile.objects.get(slug="rahul").image_path, "profiles/images/Rahul.jpg")

        admin_user = get_user_model().objects.create_superuser(
            username="separate-profile-admin",
            email="separate-profile-admin@example.test",
            password="separate-profile-test-password",
        )
        self.client.force_login(admin_user)
        for model_name in ("brideprofile", "groomprofile"):
            with self.subTest(model=model_name):
                response = self.client.get(reverse(f"admin:main_{model_name}_changelist"))
                self.assertEqual(response.status_code, 200)
        self.assertNotIn("main_curatedprofile", admin.site._registry)

        for path, name in (("/bride/", "Ankita Sharma"), ("/groom/", "Rahul Verma")):
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, name)

    def test_admin_can_add_bride_and_groom_in_their_separate_sections(self):
        admin_user = get_user_model().objects.create_superuser(
            username="separate-profile-add-admin",
            email="separate-profile-add-admin@example.test",
            password="separate-profile-test-password",
        )
        self.client.force_login(admin_user)
        for model, model_name, gender, slug, name in (
            (BrideProfile, "brideprofile", "bride", "admin-added-bride", "Admin Added Bride"),
            (GroomProfile, "groomprofile", "groom", "admin-added-groom", "Admin Added Groom"),
        ):
            with self.subTest(gender=gender):
                response = self.client.post(
                    reverse(f"admin:main_{model_name}_add"),
                    {
                        "name": name,
                        "slug": slug,
                        "is_sample": "on",
                        "profession": "Designer",
                        "location": "Kolkata",
                        "about": "A profile managed by an administrator.",
                        "expectations": "A thoughtful partner.",
                        "family": "A supportive family.",
                        "image_path": "main/images/Ankita.jpeg",
                        "_save": "Save",
                    },
                )

                self.assertEqual(response.status_code, 302)
                profile = model.objects.get(slug=slug)
                self.assertIsNone(profile.user)
                listing = self.client.get(reverse(gender))
                self.assertContains(listing, name)
                self.assertContains(
                    self.client.get(reverse("extra_profile", args=(slug,))),
                    "A profile managed by an administrator.",
                )
                self.assertRedirects(
                    self.client.get(reverse("profile_search"), {"q": name}),
                    reverse("extra_profile", args=(slug,)),
                    fetch_redirect_response=False,
                )


class AdminProfilePhotoTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.profile_user = user_model.objects.create_user(username="admin-profile-owner")
        self.admin_user = user_model.objects.create_superuser(
            username="profile-admin",
            email="admin@example.com",
            password="test-password",
        )
        self.client.force_login(self.admin_user)

    def test_admin_saves_uploaded_bride_and_groom_photos(self):
        for model, admin_route, name in (
            (GroomProfile, "admin:main_groomprofile_add", "Admin Test Groom"),
            (BrideProfile, "admin:main_brideprofile_add", "Admin Test Bride"),
        ):
            with self.subTest(profile_type=model.__name__):
                image_buffer = BytesIO()
                Image.new("RGB", (1, 1), color="white").save(image_buffer, format="PNG")
                image = SimpleUploadedFile(
                    "profile.png",
                    image_buffer.getvalue(),
                    content_type="image/png",
                )
                form_data = {
                    "user": self.profile_user.pk,
                    "name": name,
                    "profession": "Designer",
                    "location": "Kolkata",
                    "about": "A profile created in the admin.",
                    "expectations": "Kind and thoughtful partner.",
                    "family": "A close family.",
                    "photo": image,
                    "_save": "Save",
                }

                with TemporaryDirectory() as media_root:
                    with override_settings(MEDIA_ROOT=media_root):
                        response = self.client.post(reverse(admin_route), form_data)

                        self.assertEqual(response.status_code, 302)
                        profile = model.objects.get(name=name)
                        self.assertTrue(profile.photo.name)
                        self.assertTrue(profile.photo.storage.exists(profile.photo.name))

    def test_admin_profile_photo_is_not_required_for_either_profile_type(self):
        for model in (GroomProfile, BrideProfile):
            with self.subTest(profile_type=model.__name__):
                admin_model = admin.site._registry[model]
                form_class = admin_model.get_form(SimpleNamespace(user=self.admin_user))

                self.assertFalse(form_class().fields["photo"].required)
