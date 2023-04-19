from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from chuus import settings
from django.db import models
from django_quill.fields import QuillField


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("회원가입은 이메일을 필요로합니다")

        email = self.normalize_email(email)
        user = self.model(email=email,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,**extra_fields):
        user = self.create_user(email, password )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null= True, blank=True)
    name = models.CharField(max_length=255, null=True)
    profile_image = models.ImageField(editable=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    instagram = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.email
    
class EarlyBird(models.Model):
    email = models.EmailField(max_length=255, null=True)
    instagram = models.CharField(max_length=255, null=True, default=None)
    
class Campaign(models.Model): 
    name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    count =  models.IntegerField(default = 0)
    price =  models.IntegerField(default = 0)
    before_price =  models.IntegerField(default = 0)
    due_date = models.DateTimeField(auto_now_add=False, null=True)
    channel = models.CharField(max_length=255, null=True)
    mission = QuillField()
    hashtag = models.CharField(max_length=255, null=True)
    accounttag = models.CharField(max_length=255, null=True)
    info = QuillField()

class CampaignOption(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True)
    value = models.CharField(max_length=255, null=True)
    
class Influencer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="influencers", on_delete=models.CASCADE, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True)
    instagram = models.CharField(max_length=255, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    
class Post(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True)
    post_image = models.ImageField(editable=True, null=True, blank=True)
    post_url = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    
class CampaignImage(models.Model):
    campaign = models.ForeignKey(Campaign, related_name="images", on_delete=models.CASCADE, null=True)
    image = models.ImageField(editable=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
class CampaignVideo(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True)
    video = models.FileField(upload_to='videos/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)