from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webui-home'),
    path('about/', views.about, name='webui-about'),
]
