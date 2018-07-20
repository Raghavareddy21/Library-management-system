from django.conf.urls import url
from . import views
urlpatterns ={
	url(r'^list/$',views.books,name="books"),
	url(r'^(?P<pk>[0-9]+)/$',views.booklist,name="booklist"),
	url(r'^addbooks/$',views.add_books,name="add_books"),
}
