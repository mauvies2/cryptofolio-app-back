from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.currency.permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyAsset
from .serializers import AssetSerializer, \
    PortfolioSerializer, AssetsUserSerializer, PortfolioWalletSerializer
from .models import AssetsUser, Asset, Portfolio
from blockchain.exchangerates import get_ticker
from forex_python.converter import CurrencyRates
from rest_framework import filters


class AssetsUserViewSet(viewsets.ModelViewSet):
    serializer_class = AssetsUserSerializer
    queryset = AssetsUser.objects.all()
    permission_classes = [IsOwnerOrReadOnlyAsset]


class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    @action(methods=["GET"], detail=False)
    def portfolio_wallet(self, request, *args, **kwargs):
        queryset = Portfolio.objects.get(user=request.user)
        serializer = PortfolioWalletSerializer(queryset)
        return Response(serializer.data)


class AssetViewSet(viewsets.ModelViewSet):
    serializer_class = AssetSerializer
    queryset = Asset.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['cod', 'name']

    @action(detail=False, url_name="daily_btc_price_currency")
    def get_all_bitcoin_price(self, request, *args, **kwargs):
        response = list(map(lambda x: {x[0]: x[1].__dict__}, get_ticker().items()))

        return Response(response, status.HTTP_200_OK)

    @action(detail=False, url_name="daily_price_currency")
    def get_all_daily_price(self, request, *args, **kwargs):
        c = CurrencyRates()
        response = c.get_rates('USD')

        return Response(response, status.HTTP_200_OK)
