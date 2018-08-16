from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.books)
admin.site.register(models.category)
