from api import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import login, logout

from django.template import loader
from rest_framework.authtoken.models import Token
from django.http import HttpResponse

class CampaignInfluencerPageView(TemplateView):
    template_name = "campaign/campaign_influencer.html"
    
    def get(self, request, *args, **kwargs):
        print(request)
        ctx = {
        }
        return self.render_to_response(ctx)
    
    def post(self, request, *args, **kwargs):
        print(request)
        campaign = models.Campaign.objects.get(pk = kwargs['pk'])
        influencer = models.Influencer()
        influencer.user = request.user
        influencer.campaign = campaign
        influencer.save()
        ctx = {
        }
        return HttpResponse('Hello world!')


class CampaignDetailPageView(TemplateView):
    template_name = "campaign/campaign_detail.html"
    def get(self, request, *args, **kwargs):
        print(request)
        campaigns = models.Campaign.objects.all().order_by('?')[:4]
        
        campaign = models.Campaign.objects.get(pk = kwargs['pk'])
        images = models.CampaignImage.objects.filter(campaign = campaign)
        ctx = {
            'campaigns': campaigns,
            'campaign': campaign,
            'images': images,    
        }
        return self.render_to_response(ctx)
    
class CampaignApplyPageView(TemplateView):
    template_name = "campaign/campaign_detail.html"
    def post(self, request, *args, **kwargs):
        print(request)
        campaign = models.Campaign.objects.get(pk = kwargs['pk'])
        influencer = models.Influencer.objects.get(user = request.user)
        ctx = {
            'campaigns': campaigns,
            'campaign': campaign,
            'images': images,    
        }
        return self.render_to_response(ctx)
    
    
class CampaignListPageView(TemplateView):
    template_name = "campaign/campaign_list.html"
    def get(self, request, *args, **kwargs):
        print(request)
        campaigns = models.Campaign.objects.all()
        ctx = {
            'campaigns': campaigns,
        }
        return self.render_to_response(ctx)