from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

class BlogTets(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username='user',
            email='user@email.com',
            password='123'
        )
        
        cls.post = Post.objects.create(
            author=cls.user,
            title='title',
            body='nice body'
        )
    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'user')
        self.assertEqual(self.post.title, 'title')
        self.assertEqual(self.post.body, 'nice body')