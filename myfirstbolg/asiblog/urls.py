from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [

	#url(r'^start/$',views.startView , name ='start')
	url(r'^$',login_required(views.MainView.as_view()) , name='index'),
	url(r'^(?P<pk>[0-9]+)/edit/$',login_required(views.PostUpdate.as_view()),name='edit'),
	url(r'^(?P<pk>[0-9]+)/delete/$',login_required(views.SoftDelete.as_view()),name='delete'),
	url(r'^add/$',views.PostCreat.as_view(),name='addPost'),	
]