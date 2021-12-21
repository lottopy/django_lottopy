from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='homepage'),
    path('', views.home, name='lottopy'),
    path('about/', views.about, name="about"),
]
