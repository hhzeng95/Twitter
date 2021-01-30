from django.contrib.auth import get_user_model
from rest_framework import authentication


User = get_user_model()

class DevAuthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        ce = User.objects.filter(id=2)
        user = ce.order_by("?").first()
        return (user, None)
