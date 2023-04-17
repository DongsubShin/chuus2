from django.shortcuts import render
from api import models
from django.views.generic import TemplateView
from datetime import date, timedelta
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.http import HttpResponse
  

    

    
class CampaignDetailPage(TemplateView):
    template_name = "dashboard/campaign/detail.html"
    def get(self, request, *args, **kwargs):
        user = models.User.objects.get(pk=self.kwargs['pk'])
        ctx = {
            'user': user,
        }
        return self.render_to_response(ctx)

        
    
class CampaignEditPage(TemplateView):
    template_name = "dashboard/campaign/edit.html"
    def get(self, request, *args, **kwargs):
        user = models.User.objects.get(pk=self.kwargs['pk'])
        
        ctx = {
            'user': user,
        
        }
        return self.render_to_response(ctx)
    
    

    

class CampaignListPage(TemplateView):
    template_name = "dashboard/campaign/list.html"
    def get(self, request, *args, **kwargs):
        campaigns = models.Campaign.objects.all()
        ctx = {
            'campaigns': campaigns,
    
        }
        return self.render_to_response(ctx)
    

