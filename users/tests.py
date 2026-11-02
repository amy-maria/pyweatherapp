from unittest.mock import patch
from django.db.utils import OperationalError
from django.test import TestCase
from django.urls import reverse

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
