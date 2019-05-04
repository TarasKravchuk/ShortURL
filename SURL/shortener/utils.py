import string, random
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def surl_generator (size=SHORTCODE_MIN, chars = string.ascii_lowercase + string.digits):
    new_code = ''
    for i in  range(size):
        new_code += random.choice(chars)
    return new_code

def create_shortcode(instance, size=SHORTCODE_MIN):
    new_code = surl_generator(size=size)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code
