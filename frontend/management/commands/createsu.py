from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not get_user_model().objects.filter(username="CERPI220 ").exists():
            get_user_model().objects.create_superuser("CERPI220", "CERPI220@gmurano.com", "GMurano2021")