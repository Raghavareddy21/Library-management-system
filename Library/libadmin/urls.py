from django.conf.urls import url
from . import views
urlpatterns =[
	
	url(r'^(?P<pk>[0-9]+)/$', views.categorylist, name="list_song"),
	url(r'^Home/$',views.categorylist,name="categorylist"),
	url(r'^addcategory/$',views.add_category,name="add_category"),
	url(r'^booklist/$',views.booklist,name="booklist"),
	url(r'^addbook/$',views.add_books,name="add_books"),
]
