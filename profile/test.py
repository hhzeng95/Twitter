from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Profile


User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='a', password='123')
        self.userb = User.objects.create_user(username='b', password='456')
    
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='123')
        return client

    def test_profile_created_via_signal(self):
        ce = Profile.objects.all()
        self.assertEqual(ce.count(), 2)
