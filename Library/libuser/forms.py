from django import forms
from django.contrib.auth.models import User
from . import models
class placerequest(forms.ModelForm):
	class Meta:
		model=models.placerequest
		fields=('Username','book_category','book','request_date')