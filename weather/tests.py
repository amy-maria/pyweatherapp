from django.test import TestCase, Client
from django.urls import reverse


class WeatherViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view_get(self):
        response = self.client.get(reverse("home"))  # Adjust if 'home' is not the name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "")  # adjust to match page content

    def test_home_view_post_valid_city(self):
        response = self.client.post(reverse("home"), {"city": "New York"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Weather in New York")  # match template logic
