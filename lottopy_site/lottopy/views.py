# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import os
import csv

#f = "~/projects/django_lottopy/lottopy_site/lottopy/lottopy_web_edititon/pb_ans.csv"

#def files(f):
#    reader = csv.DictReader(open(f))
#    for row in reader:
#        global numbers, pb, chance
#        numbers = row[0-5]
#        pb = row[6]
#        chance = row[7]
#        pbdata = pbdata(numbers=numbers,pb=pb,chance=chance)
#        pbdata.save()

def base(request):
    return render(request, 'lottopy/base.html',
    {'nbar': 'home'})

def home(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir,'lottopy_web_edition/pb_ans.csv')
    pb = csv.reader(file_path)
    for row in pb:
        numbers = list(pb)
    context = {'nbar': 'home', 'numbers': numbers}
    return render(request, 'lottopy/home.html', context)

def about(request):
    return render(request, 'lottopy/about.html',
    {'nbar': 'about', 'title': 'About'})
