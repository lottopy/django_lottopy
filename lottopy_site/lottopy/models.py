from django.db import models
from datetime import datetime
from django.core.mail import send_mail
import os, csv

# Create your models here.
class Lotto():
    module_dir = os.path.dirname(__file__)
    names = list(["pb", "mm", "la", "d3", "d4", "c25"])
    files = []
    for i in names:
        files.append(os.path.join(module_dir,"lottopy_web_edition",i+"_ans.csv"))
        files = [i for i in files if os.path.isfile(i)]
    
    def get_ans(f):
            ans = csv.DictReader(open(f), delimiter=',')
            fmt = [str(k)[1:-1].replace("'"," ").replace("_"," ") for k in ans]
            return str(fmt).replace(",","\n").replace("[","").replace("]","").replace("'","")

class Subscribers(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Subscribers"

class MailMessage(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField(null=True)
    attachment = models.FileField(default=None, null=True, blank=True)
    users = models.ManyToManyField(Subscribers)
    send_it = models.BooleanField(default=False) # check to send email

    def save(self):
        if self.send_it:
            user_list = []
            for user in self.users.all():
                user.email_user(self.subject, self.body, self.attachment)
                send_mail(str(self.subject),
                      str(self.body),
                      'admin@wvlotterypredictor.xyz',
                      user_list,
                      fail_sliently=False)

    def __str__(self):
        return self.subject
    
    class Meta:
        verbose_name = "Emails to send"
        verbose_name_plural = "Emails to send"

    
