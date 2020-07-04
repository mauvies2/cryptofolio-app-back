# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers

from apps.users.views import UserViewSet, UserCreateViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'create_user', UserCreateViewSet)
