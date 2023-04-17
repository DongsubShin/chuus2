from django.shortcuts import render
from api import models
from django.views.generic import TemplateView
from datetime import date, timedelta
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.http import HttpResponse
  

    

    
class UserDetailPage(TemplateView):
    template_name = "dashboard/user/detail.html"
    def get(self, request, *args, **kwargs):
        user = models.User.objects.get(pk=self.kwargs['pk'])
        ctx = {
            'user': user,
        }
        return self.render_to_response(ctx)

        
    
class UserEditPage(TemplateView):
    template_name = "dashboard/user/edit.html"
    def get(self, request, *args, **kwargs):
        user = models.User.objects.get(pk=self.kwargs['pk'])
        
        ctx = {
            'user': user,
        
        }
        return self.render_to_response(ctx)
    
    

    

class UserListPage(TemplateView):
    template_name = "dashboard/user/list.html"
    def get(self, request, *args, **kwargs):
        users = models.User.objects.all()
        ctx = {
            'users': users,
    
        }
        return self.render_to_response(ctx)
    


class UserExport(TemplateView):
    def get(self, request, *args, **kwargs):         # request.POST 객체에서 데이터 얻기
        users = models.User.objects.all()
        dataset = UserResource().export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="User.csv"'
    
        return response
