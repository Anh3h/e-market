from django.urls import path

from . import views

app_name = "online_market"
urlpatterns = [
    path('', views.profile, name='profile'),
    path('password', views.password, name='password')
]