from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Tweet
# Create your tests here.
User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='t1', password='123')
        self.userb = User.objects.create_user(username='t2', password='345')
        Tweet.objects.create(content="test1", 
            user=self.user)
        Tweet.objects.create(content="test2", 
            user=self.user)
        Tweet.objects.create(content="test2", 
            user=self.userb)
        self.currentCount = Tweet.objects.all().count()
        
    def test_tweet_created(self):
        tweet_obj = Tweet.objects.create(content="test3", 
            user=self.user)
        self.assertEqual(tweet_obj.id, 4)
        self.assertEqual(tweet_obj.user, self.user)
        
    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/api/main/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
    
    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/main/action/", 
            {"id": 1, "action": "like"})
        like_count = response.json().get("likes")
        user = self.user
        my_like_instances_count = user.tweetlike_set.count()
        my_related_likes = user.tweet_user.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(like_count, 1)
        self.assertEqual(my_like_instances_count, 1)
        self.assertEqual(my_like_instances_count, my_related_likes)
