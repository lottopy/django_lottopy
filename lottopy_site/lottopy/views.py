# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from .models import Lotto

#f = "~/projects/django_lottopy/lottopy_site/lottopy/lottopy_web_edititon/pb_ans.csv"

# MAKE SURE TO START REDIS BEFORE SITE LOADS
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def base(request):
    return render(request, 'lottopy/base.html',
    {'nbar': 'home'})

@cache_page(CACHE_TTL)
def home(request):    
    
    context = {
        'nbar': 'home',
        'pbnumbers': Lotto.get_ans(Lotto.files[0]),
        'mmnumbers': Lotto.get_ans(Lotto.files[1]),
        'lanumbers': Lotto.get_ans(Lotto.files[2]),
        'd3numbers': Lotto.get_ans(Lotto.files[3]),
        'd4numbers': Lotto.get_ans(Lotto.files[4]),
        'c25numbers': Lotto.get_ans(Lotto.files[5]),
        }

    return render(request, 'lottopy/home.html', context)

@cache_page(CACHE_TTL)
def about(request):
    return render(request, 'lottopy/about.html',
    {'nbar': 'about', 'title': 'About'})

@cache_page(CACHE_TTL)
@require_GET
def robots_txt(require_GET):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def sitemap(request):
    return render(request,sitemaps,section=None,template_name='sitemap.xml',content_type='application/xml',)
    