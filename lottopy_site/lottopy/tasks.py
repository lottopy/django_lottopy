import os, csv
from celery import shared_task

@shared_task()
def secret():
    string = "If you can see this, fuck off"
    return string

module_dir = os.path.dirname(__file__)

def get_ans(f):
        ans = csv.DictReader(open(f), delimiter=',')
        fmt = [str(k)[1:-1].replace("'"," ").replace("_"," ") for k in ans]
        return str(fmt).replace(",","\n").replace("[","").replace("]","").replace("'","")

all_nums = []

@shared_task()
class data_task():
    def __init__():
        pb_file_path = os.path.join(module_dir,'lottopy_web_edition/pb_ans.csv')
        mm_file_path = os.path.join(module_dir,'lottopy_web_edition/mm_ans.csv')
        la_file_path = os.path.join(module_dir,'lottopy_web_edition/la_ans.csv')
        d3_file_path = os.path.join(module_dir,'lottopy_web_edition/d3_ans.csv')
        d4_file_path = os.path.join(module_dir,'lottopy_web_edition/d4_ans.csv')
        c25_file_path = os.path.join(module_dir,'lottopy_web_edition/c25_ans.csv')
        data_task.all_nums.append(pb_file_path, mm_file_path, la_file_path, d3_file_path, d4_file_path, c25_file_path)

        return get_ans(all_nums)
        #return pbnumbers, mmnumbers, lanumbers, d3numbers, d4numbers, c25numbers