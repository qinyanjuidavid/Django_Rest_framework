from django.contrib.auth.models import User
from posting.models import BlogPost
from rest_framework.test import APITestCase


class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username="testdayuser", email="test@test.com")
        user_obj.set_password("somerandompassword")
        user_obj.save()
        blog_post = BlogPost.objects.create(
            user=user_obj, title="New title", content="Some random content")

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = BlogPost.objects.count()
        self.assertEqual(post_count, 1)
