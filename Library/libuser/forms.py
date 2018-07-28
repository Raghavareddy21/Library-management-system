from django import forms
from django.contrib.auth.models import User
from . import models
class placerequest(forms.ModelForm):
	class Meta:
		model=models.placerequest
		fields=('book_category','book','request_date','submition_date')
	def clean_date(self):
		data=self.cleaned_data['request_date']
		check = User.objects.filter(request_date=user)
		if check.count()>0 or :
			raise ValidationError(_('The book has already been issued to someone'))
