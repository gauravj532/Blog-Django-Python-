"""myfirstbolg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import django.contrib.auth.urls 
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views
from asiblog.views import Register_success, Register_user
from asiblog.api import PostResource

post_resource = PostResource()

urlpatterns = [
	url(r'^asiblog/', include('asiblog.urls',namespace="asiblog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', "asiblog.views.login"),
    url(r'^accounts/auth_view/$',"asiblog.views.auth_view"),
    url(r'^accounts/logout/$',"asiblog.views.logoutme"), 
    url(r'^accounts/register/$',Register_user.as_view()),
    url(r'^account/register_success/$',Register_success.as_view()),
    url(r'^api/', include(post_resource.urls)),
    #url('^', include('django.contrib.auth.urls'))
]
