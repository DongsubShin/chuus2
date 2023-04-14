from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from chuus import settings
from django.db import models

# class UserManager(BaseUserManager):

#     def create_user(self, email, is_male, password=None):
#         if not email:
#             raise ValueError("회원가입은 이메일을 필요로합니다")

#         email = self.normalize_email(email)
#         user = self.model(email=email, is_male=is_male)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(email, name, True, password )
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)

#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True, null= True, blank=True)
#     name = models.CharField(max_length=255, null=True)
#     profile_image = models.ImageField(editable=True, null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     instagram = models.CharField(max_length=255, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
    
#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']
    
#     def __str__(self):
#         return self.email
    
class EarlyBird(models.Model):
    email = models.EmailField(max_length=255, null=True)
    instagram = models.CharField(max_length=255, null=True, default=None)