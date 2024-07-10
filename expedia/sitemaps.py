import datetime

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    protocol = 'https'
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return [ 'home', 'boardList', 'boardView']

    def location(self, item):
        return reverse(item)

    def lastmod(self, obj):
        return datetime.date.today()