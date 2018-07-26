# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here



def login_user(request):
    if request.user.is_authenticated:
        return HttpResponse("you are already logged in")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,
             password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/libadmin/Home/')
                else:
                    return render(request, 'adminauth/login.html', {'err': 'Your account is banned'})
            else:
                return render(request, 'adminauth/login.html', {'err': 'Wrong credentials provided'})
        else:
            return render(request, 'adminauth/login.html', {'err': ''})
def home(request):
    return render(request, 'adminauth/home.html')
#this setting file is a sample one need to edit tomorrow
# def setting(request):
#     if request.user.is_authenticated():
#         if request.method == 'POST':
#              form = DocumentForm(request.POST, request.FILES)
#              if form.is_valid():
#                  form.save()
#         else:
#             form = DocumentForm()
#              return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })
#     else:
#         return HttpResponse("you are already logged in")
