from urllib.parse import parse_qs, urlencode, urlparse

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AccessControlTests(TestCase):
    def test_homepage_and_account_entry_pages_are_public(self):
        for route in ("index", "signup", "login"):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertEqual(response.status_code, 200)

    def test_application_pages_search_and_profile_links_require_login(self):
        protected_paths = (
            reverse("about"),
            reverse("contact"),
            reverse("success_stories"),
            reverse("bride"),
            reverse("groom"),
            reverse("profile_search") + "?q=Ankita",
            reverse("profile_name_suggestions") + "?q=An",
            "/profiles/ankita/",
            reverse("extra_profile", args=("ankita",)),
            reverse("work"),
            reverse("firstlook"),
            reverse("mehendi"),
            reverse("hand"),
        )

        for path in protected_paths:
            with self.subTest(path=path):
                response = self.client.get(path)

                self.assertEqual(response.status_code, 302)
                login_url = urlparse(response["Location"])
                self.assertEqual(login_url.path, reverse("login"))
                self.assertEqual(parse_qs(login_url.query).get("next"), [path])

    def test_successful_login_returns_to_the_protected_page(self):
        get_user_model().objects.create_user(
            username="redirect-member",
            password="StrongPassword-482!",
        )
        protected_path = reverse("hand")

        response = self.client.post(
            reverse("login") + f"?next={protected_path}",
            {
                "u_name": "redirect-member",
                "u_password": "StrongPassword-482!",
                "next": protected_path,
            },
        )

        self.assertRedirects(response, protected_path, fetch_redirect_response=False)

    def test_login_rejects_external_next_redirect(self):
        get_user_model().objects.create_user(
            username="safe-redirect-member",
            password="StrongPassword-482!",
        )

        response = self.client.post(
            reverse("login"),
            {
                "u_name": "safe-redirect-member",
                "u_password": "StrongPassword-482!",
                "next": "https://attacker.example/",
            },
        )

        self.assertRedirects(
            response,
            reverse("index"),
            fetch_redirect_response=False,
        )

    def test_signup_preserves_a_safe_requested_page_for_the_later_login(self):
        protected_path = reverse("hand")

        signup_page = self.client.get(
            reverse("signup") + "?" + urlencode({"next": protected_path})
        )
        self.assertContains(signup_page, 'name="next"')

        signup_response = self.client.post(
            reverse("signup") + "?" + urlencode({"next": protected_path}),
            {
                "username": "signup-redirect-member",
                "email": "signup-redirect@example.com",
                "password1": "StrongPassword-482!",
                "password2": "StrongPassword-482!",
                "next": protected_path,
            },
        )

        self.assertRedirects(
            signup_response,
            reverse("login") + "?" + urlencode({"next": protected_path}),
            fetch_redirect_response=False,
        )


class SignUpTests(TestCase):
    def test_valid_signup_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newmember",
                "email": "newmember@example.com",
                "password1": "StrongPassword-482!",
                "password2": "StrongPassword-482!",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("login"))
        response = self.client.get(response.url)
        self.assertContains(response, "Your account has been created.")
        user = get_user_model().objects.get(username="newmember")
        self.assertEqual(user.email, "newmember@example.com")
        self.assertTrue(user.check_password("StrongPassword-482!"))

    def test_signup_shows_password_mismatch(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newmember",
                "email": "newmember@example.com",
                "password1": "StrongPassword-482!",
                "password2": "DifferentPassword-591!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The two password fields didn’t match.")
        self.assertFalse(get_user_model().objects.filter(username="newmember").exists())

    def test_signup_shows_duplicate_email_error(self):
        get_user_model().objects.create_user(
            username="existingmember",
            email="member@example.com",
            password="StrongPassword-482!",
        )

        response = self.client.post(
            reverse("signup"),
            {
                "username": "newmember",
                "email": "MEMBER@example.com",
                "password1": "StrongPassword-482!",
                "password2": "StrongPassword-482!",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An account with this email already exists.")
        self.assertFalse(get_user_model().objects.filter(username="newmember").exists())

    def test_empty_signup_post_shows_required_field_errors(self):
        response = self.client.post(reverse("signup"), {})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertContains(response, "Please correct the highlighted fields")

    def test_password_requirements_are_shown_on_signup_form(self):
        response = self.client.get(reverse("signup"))

        self.assertContains(response, "at least 8 characters")
        self.assertContains(response, "can’t be a commonly used password")
        self.assertContains(response, "can’t be entirely numeric")

    def test_weak_password_displays_validator_errors(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newmember",
                "email": "newmember@example.com",
                "password1": "12345678",
                "password2": "12345678",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "can’t be entirely numeric")
        self.assertContains(response, "Please correct the highlighted fields")
        self.assertIn("password1", response.context["form"].errors)
        self.assertNotIn("password2", response.context["form"].errors)
        self.assertFalse(get_user_model().objects.filter(username="newmember").exists())
