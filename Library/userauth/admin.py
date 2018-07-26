# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
# Register your models here.
ADMIN_VIEW_PERMISSION_MODELS = [
    'auth.User',
    'libadmin.category',
    'libadmin.books',
]
admin.site.register(models.Otherdetail)
