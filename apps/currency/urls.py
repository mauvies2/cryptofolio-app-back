# Routers provide an easy way of automatically determining the URL conf.
from django.conf.urls import url, include
from rest_framework import routers

from .views import PortfolioViewSet, AssetViewSet, \
    AssetsUserViewSet

router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioViewSet)
router.register(r'asset', AssetViewSet)
router.register(r'asset_user', AssetsUserViewSet)
