from django.core.management import BaseCommand
from django.db.utils import IntegrityError
import requests
from apps.currency.models import Asset, AssetTimeline


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from a API into our models"

    def handle(self, *args, **options):

        if Asset.objects.exists() or AssetTimeline.objects.exists():
            print('Data already loaded...exiting.')
            return
        print("Creating asset data")
        key = "45A83179-F3CC-4993-AD28-AD474A487F08"
        url = 'https://rest.coinapi.io/v1/assets'
        headers = {'X-CoinAPI-Key': key}
        response = requests.get(url, headers=headers)
        assets = response.json()
        url = "https://s3.eu-central-1.amazonaws.com/bbxt-static-icons/type-id/png_512/{id_icon}.png"
        for asset in assets:
            try:
                custom_url = url.format(id_icon=asset["id_icon"].replace('-', ''))
            except KeyError:
                custom_url = None
            try:
                obj = {
                    "name": asset["name"],
                    "price": asset["price_usd"],
                    "cod": asset["asset_id"],
                    "logo": custom_url
                }
                a = Asset.objects.create(**obj)
                b = AssetTimeline.objects.create(asset=a, price=asset["price_usd"])
                print("Objects created")
                print(a)
                print(b)
            except (KeyError, IntegrityError):
                pass
