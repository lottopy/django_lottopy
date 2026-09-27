from django.urls import path
from lottopy import views
from django.views.generic.base import TemplateView
from .views import zipdownload

urlpatterns = [
    #path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('links/', views.links, name="links"),
    path('links/modpack', views.zipdownload, name="zipdownload"),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain") , name='robots.txt'),
]
