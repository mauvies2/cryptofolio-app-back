from .models import Portfolio, Asset, AssetsUser
from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS
from apps.users.serializers import UserSimpleSerializer


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ALL_FIELDS


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ("id", "name", "cod", "logo", "price")


class AssetsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsUser
        fields = ("id", "assets_in", "balance", "portfolio")


class AssetsUserWalletSerializer(serializers.ModelSerializer):
    assets_in = AssetSerializer()

    class Meta:
        model = AssetsUser
        fields = ("id", "assets_in", "balance", "portfolio")


class PortfolioWalletSerializer(serializers.ModelSerializer):
    assets = AssetsUserWalletSerializer(many=True)
    total = serializers.SerializerMethodField()
    user = UserSimpleSerializer

    class Meta:
        model = Portfolio
        fields = ("id", "user", "assets", "total")

    def get_total(self, obj, *args, **kwargs):
        if obj.assets:
            return sum([asset.balance * asset.assets_in.price for asset in obj.assets.all()])
        else:
            return 0
