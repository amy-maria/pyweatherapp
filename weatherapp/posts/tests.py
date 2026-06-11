from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test12345", password="12pass3new"
        )

    def test_post_creation(self):
        post = Post(
            title="Test Title",
            body="Some content",
            author=self.user,
        )
        post.save()
        self.assertEqual(post.title, "Test Title")
        self.assertEqual(post.slug, "test-title")  # slug is auto-created
        self.assertEqual(str(post), "Test Title")
