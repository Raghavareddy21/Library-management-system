from django import forms
from django.contrib.auth.models import User
from libuser import models as model
from . import models

class BookaddForm(forms.ModelForm):
	class Meta:
		model = models.books
		fields =('book_category','Title','Author','image','book','date','upload_date')

class add_category(forms.ModelForm):
	class Meta:
		model = models.category
		fields=('name','about','img','date','upload_date')


class notification(forms.ModelForm):
	class Meta:
		model=model.placerequest
		fields=('accept',)
		