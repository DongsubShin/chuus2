from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register('earlyBird', views.EarlyBirdViewSet)
router.register('campaign', views.CampaignViewSet)
router.register('influencer', views.InfluencerViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
