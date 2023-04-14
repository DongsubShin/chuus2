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
    path('products/<int:pk>/', views.ProductDetailPageView.as_view(), name='detail'),
    path('accounts/', include('allauth.urls')),

 
]

