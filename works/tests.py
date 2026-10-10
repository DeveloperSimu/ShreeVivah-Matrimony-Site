from io import BytesIO
from tempfile import TemporaryDirectory

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from PIL import Image

from .models import Firstlook, MehendiCategory, MehendiDesign


class HaldiPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.member = get_user_model().objects.create_user(
            username="haldi-member",
        )

    def test_haldi_page_keeps_video_hero_and_renders_ceremony_gallery(self):
        self.client.force_login(self.member)
        response = self.client.get(reverse("haldi"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "works/videos/haldi2.mp4")
        self.assertContains(response, "A little turmeric.")
        self.assertContains(response, "works/images/haldi/haldi8.jpeg")
        self.assertContains(response, 'class="ritual-image-trigger"')
        self.assertContains(response, 'class="haldi-lightbox"')
        self.assertContains(response, "works/js/haldi.js")
        self.assertContains(response, "Tradition, told")
        self.assertNotContains(response, "haldiCountdown")


class FirePageTests(TestCase):
    def test_fire_page_uses_existing_video_and_renders_ritual_content(self):
        member = get_user_model().objects.create_user(username="fire-member")
        self.client.force_login(member)
        response = self.client.get(reverse("fire"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "works/videos/fire.mp4")
        self.assertContains(response, "autoplay muted loop playsinline")
        self.assertContains(response, "works/images/fire/agnihotra.jpeg")
        self.assertContains(response, "works/images/fire/havan.jpeg")
        self.assertContains(response, "works/images/fire/yajna.jpeg")
        self.assertContains(response, 'class="fire-dialog"')
        self.assertContains(response, "works/js/fire.js")
        self.assertContains(response, "A promise made")


class TogetherPageTests(TestCase):
    def test_together_page_renders_life_journey_and_clickable_memory_gallery(self):
        member = get_user_model().objects.create_user(username="together-member")
        self.client.force_login(member)
        response = self.client.get(reverse("together"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Growing old")
        self.assertContains(response, "works/images/together/a/a1.jpeg")
        self.assertContains(response, "works/images/together/e/e1.jpeg")
        self.assertContains(response, "works/images/together/h/hih1.jpeg")
        self.assertContains(response, 'class="memory-lightbox"')
        self.assertContains(response, "works/js/together.js")
        self.assertNotContains(response, "Share Your Story")


class HandPageTests(TestCase):
    def test_hand_page_keeps_all_couple_cards_and_controls(self):
        member = get_user_model().objects.create_user(username="hand-member")
        self.client.force_login(member)
        response = self.client.get(reverse("hand"))

        self.assertEqual(response.status_code, 200)
        for card_title in (
            "Compatibility Score",
            "Love Notes",
            "Favorite Songs Together",
            "Dream Destinations",
            "Commitment Pledge",
            "Movie Nights",
            "Anniversary Countdown",
            "Dream Home Style",
            "Pet Wishlist",
            "Memory Gallery",
            "Special Dates Reminder",
            "Fun Couple Quiz",
            "Love Quote of the Day",
            "Couple Mood Tracker",
            "Daily Gratitude",
            "Memory Vault",
            "Daily Challenge",
        ):
            with self.subTest(card_title=card_title):
                self.assertContains(response, card_title)

        for control_id in (
            "compatRange",
            "loveText",
            "songInput",
            "destChips",
            "pledgeNames",
            "movieInput",
            "anniDate",
            "homeChips",
            "petChips",
            "imgInput",
            "dateInput",
            "quizQ",
            "moods",
            "gratitude",
            "anniversaryDate",
            "memoryText",
            "newChallenge",
        ):
            with self.subTest(control_id=control_id):
                self.assertContains(response, f'id="{control_id}"')


class FirstlookPageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_model = get_user_model()
        cls.member = user_model.objects.create_user(
            username="firstlove-member",
            password="test-password",
        )
        cls.admin = user_model.objects.create_superuser(
            username="firstlove-admin",
            email="admin@example.test",
            password="test-password",
        )

    def make_image(self, name="firstlove.png"):
        image = Image.new("RGB", (2, 2), color="red")
        content = BytesIO()
        image.save(content, format="PNG")
        return SimpleUploadedFile(
            name,
            content.getvalue(),
            content_type="image/png",
        )

    def test_wedding_gallery_renders_each_remaining_collection(self):
        self.client.force_login(self.member)
        response = self.client.get(reverse("work"))

        self.assertEqual(response.status_code, 200)
        for title in (
            "First Look Reactions",
            "Mehendi Fun",
            "Haldi Glow",
            "Sacred Fire Ritual",
            "Growing Old Together",
            "Hand in Hand",
        ):
            with self.subTest(title=title):
                self.assertContains(response, title)

        self.assertNotContains(response, "Royal Couple")
        self.assertNotContains(response, "Regal Walk")
        self.assertNotContains(response, "Palace Portrait")

    def test_member_can_add_firstlove_from_gallery(self):
        with TemporaryDirectory() as media_root:
            with self.settings(MEDIA_ROOT=media_root):
                self.client.force_login(self.member)
                response = self.client.post(
                    reverse("firstlook"),
                    {
                        "title": "Mira & Dev",
                        "description": "They met at a bookshop.",
                        "image": self.make_image(),
                    },
                    follow=True,
                )

                self.assertEqual(response.status_code, 200)
                self.assertTrue(Firstlook.objects.filter(title="Mira ❤️ Dev").exists())
                self.assertContains(response, "Your Firstlove story has been added.")
                self.assertContains(response, "Mira ❤️ Dev")
                self.assertContains(response, 'id="add-firstlove" hidden')

    def test_member_can_add_story_with_very_long_uploaded_filename(self):
        long_filename = f"{'Ram and Roshni rainy day first love story ' * 5}.png"
        self.assertGreater(len(long_filename), 100)

        with TemporaryDirectory() as media_root:
            with self.settings(MEDIA_ROOT=media_root):
                self.client.force_login(self.member)
                response = self.client.post(
                    reverse("firstlook"),
                    {
                        "title": "Ram & Roshni",
                        "description": "They met at a bus shelter in the rain.",
                        "image": self.make_image(long_filename),
                    },
                    follow=True,
                )

                self.assertEqual(response.status_code, 200)
                story = Firstlook.objects.get(title="Ram ❤️ Roshni")
                self.assertLessEqual(len(story.image.name), 100)
                self.assertTrue(story.image.storage.exists(story.image.name))

    def test_firstlove_form_starts_hidden_and_page_has_no_admin_management_link(self):
        self.client.force_login(self.member)
        response = self.client.get(reverse("firstlook"))

        self.assertContains(response, "Add Firstlove")
        self.assertNotContains(response, "Manage Firstlove stories")
        self.assertNotContains(response, "/admin/works/firstlook/")
        self.assertContains(response, 'id="add-firstlove" hidden')

    def test_story_cards_include_full_story_for_dialog_and_truncated_preview(self):
        Firstlook.objects.create(
            title="Kunal ❤️ Ishita",
            description="A very long story that should be available in the popup.",
            image_path="works/images/aa6.jpeg",
        )
        self.client.force_login(self.member)

        response = self.client.get(reverse("firstlook"))

        self.assertContains(response, 'class="story-card-trigger"')
        self.assertContains(response, 'data-story-title="Kunal ❤️ Ishita"')
        self.assertContains(
            response,
            'data-story="A very long story that should be available in the popup."',
        )
        self.assertContains(response, 'id="story-dialog"')
        self.assertContains(response, "Read full story")

    def test_firstlove_form_stays_open_after_validation_error(self):
        self.client.force_login(self.member)
        response = self.client.post(
            reverse("firstlook"),
            {
                "title": "",
                "description": "Story without a title",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="add-firstlove"')
        self.assertNotContains(response, 'id="add-firstlove" hidden')
        self.assertContains(response, 'aria-expanded="true"')

    def test_only_staff_admin_can_open_django_admin(self):
        self.client.force_login(self.member)
        member_response = self.client.get(reverse("admin:works_firstlook_changelist"))
        self.assertNotEqual(member_response.status_code, 200)

        self.client.force_login(self.admin)
        admin_response = self.client.get(reverse("admin:works_firstlook_changelist"))
        self.assertEqual(admin_response.status_code, 200)


class MehendiGalleryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_model = get_user_model()
        cls.member = user_model.objects.create_user(
            username="mehendi-member",
            password="test-password",
        )
        cls.admin = user_model.objects.create_superuser(
            username="mehendi-admin",
            email="mehendi-admin@example.test",
            password="test-password",
        )
        cls.bridal = MehendiCategory.objects.get(name="Bridal")

    def make_image(self, name="design.png"):
        image = Image.new("RGB", (2, 2), color="green")
        content = BytesIO()
        image.save(content, format="PNG")
        return SimpleUploadedFile(name, content.getvalue(), content_type="image/png")

    def test_mehendi_gallery_renders_video_and_admin_managed_design_types(self):
        self.client.force_login(self.member)
        response = self.client.get(reverse("mehendi"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "class=\"hero-video\"")
        self.assertContains(response, "autoplay muted loop playsinline")
        self.assertContains(response, "Bridal")
        self.assertContains(response, "Minimal")
        self.assertContains(response, "Traditional")
        self.assertContains(response, "Arabic")
        self.assertContains(response, "Bridal floral detail 01")
        self.assertContains(response, 'class="design-image-trigger"')
        self.assertContains(response, 'class="mehendi-lightbox"')
        self.assertContains(response, "works/js/mehendi.js")

    def test_member_can_add_mehendi_design_and_it_appears_immediately(self):
        with TemporaryDirectory() as media_root:
            with self.settings(MEDIA_ROOT=media_root):
                self.client.force_login(self.member)
                response = self.client.post(
                    reverse("mehendi"),
                    {
                        "title": "Rain-inspired bridal vines",
                        "category": self.bridal.pk,
                        "description": "A fine-line bridal pattern.",
                        "image": self.make_image("a very long mehendi design filename " * 4 + ".png"),
                    },
                    follow=True,
                )

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, "Your mehendi design has been added to the gallery.")
                self.assertContains(response, "Rain-inspired bridal vines")
                self.assertContains(response, "id=\"add-design\" hidden")
                design = MehendiDesign.objects.get(title="Rain-inspired bridal vines")
                self.assertEqual(design.submitted_by, self.member)
                self.assertLessEqual(len(design.image.name), 100)
                self.assertTrue(design.image.storage.exists(design.image.name))

    def test_mehendi_form_stays_open_when_submission_is_invalid(self):
        self.client.force_login(self.member)
        response = self.client.post(
            reverse("mehendi"),
            {
                "title": "Missing photo design",
                "category": self.bridal.pk,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'id="add-design" hidden')
        self.assertContains(response, 'aria-expanded="true"')
        self.assertEqual(MehendiDesign.objects.filter(title="Missing photo design").count(), 0)

    def test_only_admin_can_manage_mehendi_types_and_designs(self):
        category_url = reverse("admin:works_mehendicategory_changelist")
        design_url = reverse("admin:works_mehendidesign_changelist")

        self.client.force_login(self.member)
        self.assertNotEqual(self.client.get(category_url).status_code, 200)
        self.assertNotEqual(self.client.get(design_url).status_code, 200)

        self.client.force_login(self.admin)
        self.assertEqual(self.client.get(category_url).status_code, 200)
        self.assertEqual(self.client.get(design_url).status_code, 200)

        category_add_url = reverse("admin:works_mehendicategory_add")
        self.assertEqual(
            self.client.post(category_add_url, {"name": "Indo-Arabic"}, follow=True).status_code,
            200,
        )
        self.assertTrue(MehendiCategory.objects.filter(name="Indo-Arabic").exists())
