# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect 
from django.contrib import messages
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from .forms import SubscribersForm
from .models import Lotto
import logging 

#f = "~/projects/django_lottopy/lottopy_site/lottopy/lottopy_web_edititon/pb_ans.csv"

# MAKE SURE TO START REDIS BEFORE SITE LOADS
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

#@cache_page(CACHE_TTL)
#def base(request):
#    return render(request, 'base.html',
#    {'nbar': 'home'})
logger = logging.getLogger(__file__)

@cache_page(CACHE_TTL)
def home(request):    
    context = {
        'nbar': 'home',
        'title': 'Home',
        'pbnumbers': Lotto.get_ans(Lotto.files[0]),
        'mmnumbers': Lotto.get_ans(Lotto.files[1]),
        'lanumbers': Lotto.get_ans(Lotto.files[2]),
        'd3numbers': Lotto.get_ans(Lotto.files[3]),
        'd4numbers': Lotto.get_ans(Lotto.files[4]),
        'c25numbers': Lotto.get_ans(Lotto.files[5]),
        }

    return render(request, 'home.html', context)

#@cache_page(CACHE_TTL)
def about(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscribed successfully')
            return redirect('/about')
    else:
        form = SubscribersForm()
    return render(request, 'about.html',
    {'nbar': 'about', 'title': 'About', 'form': form})

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
    return render(request,sitemap,section=None,template_name='sitemap.xml',content_type='application/xml',)
    
