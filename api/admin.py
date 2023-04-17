from django.contrib import admin
from api import models
# Register your models here.
admin.site.register(models.EarlyBird)
admin.site.register(models.User)
admin.site.register(models.Campaign)
admin.site.register(models.CampaignImage)
