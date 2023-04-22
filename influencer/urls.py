from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from influencer import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home', views.HomePageView.as_view(), name='home'),
    path('contact', views.ContactPageView.as_view(), name='contact'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('campaigns/', views.CampaignListPageView.as_view(), name='list'),
    path('campaigns/<int:pk>/', views.CampaignDetailPageView.as_view(), name='detail'),
    path('campaigns/<int:pk>/influencer/', views.CampaignInfluencerPageView.as_view(), name='detail'),
    
 
]

