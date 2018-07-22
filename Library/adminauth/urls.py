from django.conf.urls import url
from . import views
from django.contrib.auth import views as  authViews

urlpatterns = [

    url(r'^home/$',views.home,name="home.html"),
    url(r'^login/$', views.login_user, name="login.html"),
    url(r'^logout/$', authViews.logout, {'template_name':'adminauth/logout.html'}),
#    url(r'^login/$', views.login, name="login"),
]
