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

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):
        campaigns = models.Campaign.objects.all()

        ctx = {
            'campaigns': campaigns,    
        }
        return self.render_to_response(ctx)

    
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
    
    
class CampaignListPageView(TemplateView):
    template_name = "campaign/campaign_list.html"
    def get(self, request, *args, **kwargs):
        print(request)
        campaigns = models.Campaign.objects.all()
        ctx = {
            'campaigns': campaigns,
        }
        return self.render_to_response(ctx)

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class LoginPageView(TemplateView):
    template_name = "login.html"
