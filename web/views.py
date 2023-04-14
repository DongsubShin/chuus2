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

class PrivacyPageView(TemplateView):
    template_name = "privacy.html"

