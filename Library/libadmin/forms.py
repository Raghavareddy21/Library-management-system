from django import forms
from django.contrib.auth.models import User
from libadmin.models import models
from . import models
class BookaddForm(forms.ModelForm):
	class Meta:
		model = models.booklist
		fields =('Title','Author','Category','image')
