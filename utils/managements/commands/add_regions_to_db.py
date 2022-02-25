from django.core.management import BaseCommand

from utils.scripts.add_regions import (seed_countries, seed_states, seed_cities)


class Command(BaseCommand):
    help = "Seeding"

    def handle(self, *args, **options):
        self.stdout.write("Seeding regions started...")
        seed_countries()
        seed_states()
        seed_cities()
        self.stdout.write("Done!")
