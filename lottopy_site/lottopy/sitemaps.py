from django.contrib import sitemaps
from django.urls import reverse, path
from .views import home, about, robots_txt

class StaticViewSitemap(sitemaps.Sitemap):
    protocol = 'http'
    priority=.5,
    changefreq='weekly'

    def items(self):
        return ['home', 'about', 'robots_txt']

    def location(self, item):
        return reverse(item)