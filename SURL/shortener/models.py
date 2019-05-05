from django.db import models
from django.conf import settings
from .utils import surl_generator, create_shortcode
from django_hosts.resolvers import reverse
from .validators import validate_url

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class SURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(SURLManager, self).all(*args, **kwargs)
        #qs = qs_main.filter(active=True) !
        qs = qs_main.filter(id__gte=1)
        return qs

    def refresh_shortcodes (self, items=None):
        qs = ShortURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return f'New code made {new_codes}'


class ShortURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = SURLManager()


    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)

    def __str__ (self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path

