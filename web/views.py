from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import login, logout

from django.template import loader

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"