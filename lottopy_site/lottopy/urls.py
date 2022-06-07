from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    #path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain") , name='robots.txt'),
]
