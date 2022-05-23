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
    # Powerball 
    module_dir = os.path.dirname(__file__)
    pb_file_path = os.path.join(module_dir,'lottopy_web_edition/pb_ans.csv')
    pb = csv.DictReader(open(pb_file_path), delimiter=',')
    pb_numbers = {}
    for x in pb:
        pbnumbers = str(x)[1:-1].replace("'"," ").replace(",","\n").replace("_"," ")
        pbnumbers.capitalize()
    
    # MegaMil
    mm_file_path = os.path.join(module_dir,'lottopy_web_edition/mm_ans.csv')
    mm = csv.DictReader(open(mm_file_path), delimiter=',')
    mmnumbers = {}
    for y in mm:
        mmnumbers = str(y)[1:-1].replace("'"," ").replace(",","\n").replace("_"," ")

    # Lotto America
    la_file_path = os.path.join(module_dir,'lottopy_web_edition/la_ans.csv')
    la = csv.DictReader(open(la_file_path), delimiter=',')
    lanumbers = {}
    for z in la:
        lanumbers = str(z)[1:-1].replace("'"," ").replace(",","\n").replace("_"," ")

    # Daily3
    d3_file_path = os.path.join(module_dir,'lottopy_web_edition/d3_ans.csv')
    d3 = csv.DictReader(open(d3_file_path), delimiter=',')
    d3numbers = {}
    for a in d3:
        d3numbers = str(a)[1:-1].replace("'"," ").replace('"', " ").replace(",","\n").replace("_"," ")

    # Daily4
    d4_file_path = os.path.join(module_dir,'lottopy_web_edition/d4_ans.csv')
    d4 = csv.DictReader(open(d4_file_path), delimiter=',')
    d4numbers = {}
    for b in d4:
        d4numbers = str(b)[1:-1].replace("'"," ").replace('"', " ").replace(",","\n").replace("_"," ")

    # Cash25
    c25_file_path = os.path.join(module_dir,'lottopy_web_edition/c25_ans.csv')
    c25 = csv.DictReader(open(c25_file_path), delimiter=',')
    c25numbers = {}
    for c in c25:
        c25numbers = str(c)[1:-1].replace("'"," ").replace('"', " ").replace(",","\n").replace("_"," ")
    
    #Sanitizer (WIP)
    #for key, value in pbnumbers.items():
     #   pbnumbers = str(key)+":"+value


    context = {
        'nbar': 'home',
        'pbnumbers': pbnumbers,
        'mmnumbers': mmnumbers,
        'lanumbers': lanumbers,
        'd3numbers': d3numbers,
        'd4numbers': d4numbers,
        'c25numbers': c25numbers
        }
    return render(request, 'lottopy/home.html', context)

def about(request):
    return render(request, 'lottopy/about.html',
    {'nbar': 'about', 'title': 'About'})
