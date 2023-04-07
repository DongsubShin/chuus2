from django.db import models

# Create your models here.

class EarlyBird(models.Model):
    email = models.EmailField(max_length=255, unique=True)