from django.db import models
import os, csv

# Create your models here.
class Lotto():
    module_dir = os.path.dirname(__file__)
    names = list(["pb", "mm", "la", "d3", "d4", "c25"])
    files = list()
    for i in names:
        files.append(os.path.join(module_dir,"lottopy_web_edition",i+"_ans.csv"))
        files = [i for i in files if os.path.isfile(i)]
    
    def get_ans(f):
            ans = csv.DictReader(open(f), delimiter=',')
            fmt = [str(k)[1:-1].replace("'"," ").replace("_"," ") for k in ans]
            return str(fmt).replace(",","\n").replace("[","").replace("]","").replace("'","")