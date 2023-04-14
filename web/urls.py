from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from web import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('privacy', views.PrivacyPageView.as_view(), name='privacy'),
    
]

