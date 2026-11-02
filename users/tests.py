from unittest.mock import patch
from django.db.utils import OperationalError
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginRedirectTests(TestCase):
    def setUp(self):
        User.objects.create_user(username="amy", password="strong-password")
        
    def login_with_next(self, next_url):
        return self.client.post(
            reverse("users:login"),
            {"username": "amy", "password": "strong-password", "next": next_url},
        )
        
    def test_safe_next_url_is_followed(self):
        response = self.login_with_next("/posts/")
        self.assertRedirects(response, "/posts/", fetch_redirect_response=False)
        
    def test_external_next_url_is_ignored(self):
        response = self.login_with_next("https://evil.example/login")
        self.assertRedirects(response, reverse("home"))
    
    def test_scheme_relative_trick_is_ignored(self):
        response = self.login_with_next("//evil.example/login")
        self.assertRedirects(response, reverse("home"))
        
        
class DatabaseOutageTests(TestCase):
    def test_login_shows_friendsly_page_when_database_is_down(self):
        #pretend db is down while login page logs
        with patch(
            "users.views.AuthenticationForm.is_valid",
            side_effect=OperationalError("database is down"),
            ): response = self.client.post(reverse("users:login"), {"username": "amy", "password": "anything"},
                                       )
        self.assertEqual(response.status_code, 503)
        self.assertContains(response, "Accounts Unavailable", status_code=503)
        
    def test_other_errors_are_not_hidden(self):
        with patch(
            "users.views.AuthenticationForm.is_valid", side_effect=ValueError("a realbug"),                  
        ):
            with self.assertRaises(ValueError):
                self.client.post(
                    reverse("users:login"),
                    {"username": "amy", "password": "anything"},
                )
# Create your tests here.
