from django.shortcuts import render
from api import models
from django.views.generic import TemplateView
from datetime import date, timedelta
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

# Create your views here.
class IndexPage(TemplateView):
    template_name = "dashboard/index.html"
    
    def get(self, request, *args, **kwargs):
        users = models.User.objects.all().count()
        ctx = {'users': users,}
        return self.render_to_response(ctx)
    
    
