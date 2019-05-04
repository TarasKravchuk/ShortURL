from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ShortURL

def redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(ShortURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

class redirectCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post (self, request, *args, **kwargs):
        return HttpResponse()


def _test_view(request):
    return HttpResponse("test_view")
