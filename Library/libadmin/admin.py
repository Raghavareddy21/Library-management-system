from django.contrib import admin
from . import models
from libadmin.models import books 
# Register your models here.
def make_published(modeladmin, request, queryset):
    queryset.update(status=True)
make_published.short_description = "Mark selected books as accepted"
class ArticleAdmin(admin.ModelAdmin):
    actions = [make_published]
admin.site.register(models.books,ArticleAdmin)
admin.site.register(models.category)
