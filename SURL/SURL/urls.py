from shortener.views import redirect_view, redirectCBView, _test_view
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ololo123/', _test_view),
    url(r'^(?P<shortcode>[\w-]{6,15})/$', redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+){6,15}/$', redirectCBView.as_view()),
]


#r'^(?P<shortcode>[\w-]{6,15})/$'﻿