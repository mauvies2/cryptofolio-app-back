from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models


class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    total = models.FloatField(verbose_name="Total Balance")

    def __str__(self):
        return f"{self.user} Portfolio"

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=256, unique=True, null=True, blank=True)
    cod = models.CharField(max_length=256, unique=True)
    logo = models.URLField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"


class AssetTimeline(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    datetime = models.DateTimeField(auto_now=True)
    asset = models.ForeignKey('Asset', related_name='asset_timeline', on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        verbose_name = "Asset Timeline"
        verbose_name_plural = "Assets Timeline"


class AssetsUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    assets_in = models.ForeignKey('Asset', related_name='asset_user', on_delete=models.CASCADE)
    balance = models.FloatField()
    portfolio = models.ForeignKey('Portfolio', related_name='assets', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.portfolio.user.username} {self.assets_in.name}"

    class Meta:
        verbose_name = "User Asset"
        verbose_name_plural = "User Assets"
