from django.contrib import sitemaps
from django.urls import reverse
#from .views import home, about, robots_txt

class StaticViewSitemap(sitemaps.Sitemap):
    protocol = 'https'
    priority=.5,
    changefreq='weekly'

    def items(self):
        return ['home', 'about']

    def location(self, item):
        return reverse(item)
