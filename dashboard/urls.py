from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from dashboard import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', permission_required('IsAdmin')(views.IndexPage.as_view()), name='index'),
    path('users', permission_required('IsAdmin')(views.UserListPage.as_view()), name='index'),
    path('users/<int:pk>/', permission_required('IsAdmin')(views.UserDetailPage.as_view()), name='detail'),
    path('campaigns', permission_required('IsAdmin')(views.CampaignListPage.as_view()), name='index'),
    path('campaigns/<int:pk>/', permission_required('IsAdmin')(views.CampaignDetailPage.as_view()), name='detail'),
    
]

