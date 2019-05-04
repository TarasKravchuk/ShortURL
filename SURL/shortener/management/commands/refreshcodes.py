from django.core.management.base import CommandError, BaseCommand
from shortener.models import ShortURL

class Command (BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return ShortURL.objects.refresh_shortcodes(items=options['items'])

