from django.contrib.auth.models import User
from posting.models import BlogPost
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status


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

    def test_get_list(self):
        data = {}
        url = api_reverse("api-postings:post-list-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)

    def test_post_item(self):
        data = {
            "title": "Some random title",
            "Content": "Some more content"
        }
        url = api_reverse("api-postings:post-list-create")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
        blog_post = BlogPost.objects.first()
        data = {}
        url = blog_post.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_update_item(self):
        blog_post = BlogPost.objects.first()
        url = blog_post.get_api_url()
        data = {
            "title": "Some random title",
            "content": "some more content"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
