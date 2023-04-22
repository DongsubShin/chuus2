from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from api import models
from django.db.models import Sum, Q
from django.db.models import Avg



class EarlyBirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EarlyBird
        fields = '__all__'
        

class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Influencer
        fields = '__all__'
        
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Campaign
        fields = '__all__'