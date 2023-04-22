from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes , authentication_classes
from rest_framework.filters import SearchFilter

from django.db.models import Q,Count

from api import serializers
from api import models
from api import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from rest_framework import status
import requests

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class InfluencerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EarlyBirdSerializer
    queryset = models.Influencer.objects.all()
