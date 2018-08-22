from django import forms
from django.contrib.auth.models import User
from . import models
from libadmin import models as model
from libadmin.models import books
class placerequest(forms.ModelForm):
	class Meta:
		model=models.placerequest
		fields=('Username','book_category','book','request_date')
class BookaddForm(forms.ModelForm):
	class Meta:
		model = model.books
		fields =('book_category','Title','Author','image','book','date','upload_date')
