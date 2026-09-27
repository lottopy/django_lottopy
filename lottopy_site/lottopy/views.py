# Create your views here.
from django.http import FileResponse
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
import os

#f = "~/projects/django_lottopy/lottopy_site/lottopy/lottopy_web_edititon/pb_ans.csv"

# MAKE SURE TO START REDIS BEFORE SITE LOADS
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

#@cache_page(CACHE_TTL)
#def base(request):
#    return render(request, 'base.html',
#    {'nbar': 'home'})
logger = logging.getLogger(__file__)

def zipdownload(request):
        file_path = os.path.join(settings.STATIC_ROOT, 'files', 'mods.zip')
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='mods.zip')

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
        'cpnumbers': Lotto.get_ans(Lotto.files[6]),
        }

    return render(request, 'home.html', context)

def countrycode(request):
    country_code = request.META.get('HTTP_CF_IPCOUNTRY', 'N/A').strip()
    ip = request.META['REMOTE_ADDR']
    logger.info(country_code, ip)

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
    context = {
        'nbar': 'about', 
        'title': 'About', 
        'form': form,
        # Add these to stop the KeyError temporarily
        'tag': '',
        'form_class': '',
        'field_class': '',
        'label_class': '',
        'help_text_inline': False,
        'error_text_inline': False,
    }
    
    return render(request, 'about.html', context)

#    return render(request, 'about.html',
#            {'nbar': 'about', 'title': 'About', 'form': form})

def links(request):
    context = {
            'nbar': 'links',
            'title': 'Links',
            }
    return render(request, 'links.html', context)
        #{'nbar': 'links', 'title': 'Links'}

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
    
