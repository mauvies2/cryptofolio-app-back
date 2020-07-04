import requests
from apps.currency.models import AssetTimeline, Asset
from celery import shared_task


@shared_task
def update_currencies():
    key = "45A83179-F3CC-4993-AD28-AD474A487F08"
    url = 'https://rest.coinapi.io/v1/assets'
    headers = {'X-CoinAPI-Key': key}
    response = requests.get(url, headers=headers)
    assets = response.json()

    for asset in assets:
        try:
            print("Updated asset")
            a = Asset.objects.get(name=asset["name"], cod=asset["asset_id"])
            a.price = asset["price_usd"]
            a.save()
            print(a)
            print("Timeline Asset created")
            b = AssetTimeline.objects.create(asset=a, price=asset["price_usd"])
            print(b)
        except (Asset.DoesNotExist, KeyError, Asset.MultipleObjectsReturned):
            pass
