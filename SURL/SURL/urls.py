from shortener.views import redirectCBView, HomeView
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^b/(?P<shortcode>[\w-]+){6,15}/$', redirectCBView.as_view()),
]


#r'^(?P<shortcode>[\w-]{6,15})/$'﻿