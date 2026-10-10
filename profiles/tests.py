from pathlib import Path

from django.contrib.auth import get_user_model
from django.contrib.staticfiles import finders
from django.test import TestCase
from django.urls import reverse
from django.utils.html import escape

from main.models import BrideProfile, GroomProfile

from .profile_data import (
    EXTRA_BRIDES,
    EXTRA_GROOMS,
    EXTRA_PROFILES,
    FEATURED_BRIDES,
    FEATURED_GROOMS,
    FEATURED_PROFILES,
)


class ProfileDetailLayoutTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(username="profile-detail-viewer")
        self.client.force_login(user)

    def test_all_profile_details_use_the_shared_full_width_shell(self):
        profile_names = (
            "rahul",
            "brent",
            "matthew",
            "arjun",
            "karan",
            "ankita",
            "priya",
            "ishita",
            "neha",
            "sneha",
        )

        for profile_name in profile_names:
            with self.subTest(profile=profile_name):
                response = self.client.get(f"/profiles/{profile_name}/")

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.content.count(b'class="site-header"'), 1)
                self.assertEqual(response.content.count(b'class="site-footer"'), 1)
                self.assertContains(response, "profiles/css/user.css?v=4")
                self.assertContains(response, "profiles/js/profile-scroll.js?v=1")
    def test_featured_profile_details_and_photos_render_on_their_original_routes(self):
        self.assertEqual(len(FEATURED_BRIDES), 5)
        self.assertEqual(len(FEATURED_GROOMS), 5)

        for profile in FEATURED_PROFILES:
            with self.subTest(profile=profile["slug"]):
                response = self.client.get(f"/profiles/{profile['slug']}/")

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, profile["name"])
                self.assertContains(response, profile["profession"])
                self.assertContains(response, profile["location"])
                self.assertContains(response, escape(profile["about"]))
                self.assertContains(response, escape(profile["expectations"]))
                self.assertContains(response, escape(profile["family"]))
                self.assertContains(
                    response,
                    f"/static/{profile['photo'].replace(' ', '%20')}",
                )
                self.assertContains(response, "profiles/css/user.css?v=4")

    def test_there_are_five_sample_profiles_for_each_group_with_existing_photos(self):
        self.assertEqual(len(EXTRA_BRIDES), 5)
        self.assertEqual(len(EXTRA_GROOMS), 5)
        for profile in (*FEATURED_PROFILES, *EXTRA_PROFILES):
            with self.subTest(profile=profile["slug"]):
                image_path = finders.find(profile["photo"])
                self.assertIsNotNone(image_path)
                self.assertTrue(Path(image_path).is_file())

    def test_last_four_sample_photos_show_the_matching_gender(self):
        self.assertEqual(
            [profile["photo"] for profile in EXTRA_BRIDES[1:]],
            [
                "works/images/22.jpeg",
                "works/images/27.jpeg",
                "profiles/images/Farah.jpg",
                "works/images/haldi/haldi2.jpeg",
            ],
        )
        self.assertEqual(
            [profile["photo"] for profile in EXTRA_GROOMS[1:]],
            [
                "profiles/images/Rohan.jpg",
                "profiles/images/Imran.jpg",
                "profiles/images/Sayan.jpg",
                "profiles/images/Dev.jpg",
            ],
        )

    def test_additional_sample_profiles_show_all_details_and_photos(self):
        for profile in EXTRA_PROFILES:
            with self.subTest(profile=profile["slug"]):
                response = self.client.get(f"/profiles/details/{profile['slug']}/")

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, profile["name"])
                self.assertContains(response, profile["profession"])
                self.assertContains(response, profile["location"])
                self.assertContains(response, escape(profile["about"]))
                self.assertContains(response, escape(profile["expectations"]))
                self.assertContains(response, escape(profile["family"]))
                self.assertContains(response, f"/static/{profile['photo']}")
                self.assertEqual(response.content.count(b'class="site-header"'), 1)
                self.assertEqual(response.content.count(b'class="site-footer"'), 1)
                self.assertContains(response, "profiles/css/user.css?v=4")


class ProfileSearchTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(username="profile-search-user")
        self.client.force_login(user)
        self.bride = BrideProfile.objects.create(
            user=user,
            name="Newly Added Bride",
            profession="Architect",
            location="Kolkata",
            about="Enjoys thoughtful design and travelling.",
        )
        self.groom = GroomProfile.objects.create(
            user=user,
            name="Recently Added Groom",
            profession="Teacher",
            location="Pune",
            about="Enjoys reading and hiking.",
        )

    def test_exact_name_search_opens_new_bride_and_groom_profiles(self):
        for query, profile, detail_name in (
            ("newly added bride", self.bride, "bride_detail"),
            ("Recently Added Groom", self.groom, "groom_detail"),
        ):
            with self.subTest(query=query):
                response = self.client.get(reverse("profile_search"), {"q": query})

                self.assertRedirects(
                    response,
                    reverse(detail_name, args=(profile.pk,)),
                    fetch_redirect_response=False,
                )

    def test_partial_name_search_lists_matches_but_other_fields_do_not_match(self):
        response = self.client.get(
            reverse("profile_search"),
            {"q": "e"},
        )
        self.assertContains(response, self.bride.name)
        self.assertContains(response, self.groom.name)

        single_partial_match = self.client.get(
            reverse("profile_search"),
            {"q": "newly"},
        )
        self.assertRedirects(
            single_partial_match,
            reverse("bride_detail", args=(self.bride.pk,)),
            fetch_redirect_response=False,
        )

        no_match_response = self.client.get(
            reverse("profile_search"),
            {"q": "Architect"},
        )
        self.assertContains(no_match_response, "No profiles found matching")
        self.assertNotContains(no_match_response, self.bride.name)

    def test_name_suggestions_match_one_or_more_characters_for_both_genders(self):
        one_letter = self.client.get(
            reverse("profile_name_suggestions"),
            {"q": "n"},
        )
        self.assertEqual(one_letter.status_code, 200)
        self.assertTrue(
            any(
                profile["name"] == self.bride.name
                for profile in one_letter.json()["profiles"]
            )
        )

        two_letters = self.client.get(
            reverse("profile_name_suggestions"),
            {"q": "re"},
        )
        self.assertTrue(
            any(
                profile["name"] == self.groom.name
                for profile in two_letters.json()["profiles"]
            )
        )

        no_match = self.client.get(
            reverse("profile_name_suggestions"),
            {"q": "architect"},
        )
        self.assertEqual(no_match.json()["profiles"], [])

    def test_blank_search_does_not_list_every_profile(self):
        response = self.client.get(reverse("profile_search"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a name, profession, location, or keyword")
        self.assertNotContains(response, self.bride.name)
