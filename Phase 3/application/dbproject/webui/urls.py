from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webui-home'),
    path('insert/', views.insert, name='webui-insert'),
    path('about/', views.about, name='webui-about'),
]
