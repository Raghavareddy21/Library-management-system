from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^Home/$',views.categorylist,name="categorylist"),
	url(r'^booklist/$',views.booklist,name="booklist"),
	url(r'^add_books/$',views.add_books,name="add_books"),
	url(r'^(?P<pk>[0-9]+)/$', views.booklist, name="booklist"),
	url(r'^placerequest/$',views.placerequest,name="placerequest"),
	]
