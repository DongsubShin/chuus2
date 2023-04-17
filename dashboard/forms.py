from django import forms
from api import models
# Model Form (모델 폼)
class UserForm(forms.ModelForm):
	class Meta:
		model = models.User
		fields = ['name', 'email', 'phone']