from django.core.management import BaseCommand
from apps.currency.tasks import update_currencies


class Command(BaseCommand):
    # Show this when the user types help
    help = "Update data from a API into our models"

    def handle(self, *args, **options):
        update_currencies()
