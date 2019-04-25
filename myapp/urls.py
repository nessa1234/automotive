"""myproject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from myapp.views import HomeView,ElementView,ServicesView,GalleryView,AboutView,ContactView,RegisterCustomer,GallCreateView,EmailView,SuccessView
from django.conf.urls.static import static 
from myapp.views import GallistView

from django.conf import settings

urlpatterns = [
 url(r'^$',HomeView.as_view(),name='home'),
 url(r'element',ElementView.as_view(),name='element'),
 url(r'services',ServicesView.as_view(),name='services'),
 url(r'gallery',GalleryView.as_view(),name='gallery'),
 url(r'about',AboutView.as_view(),name='about'),
 url(r'contact',ContactView.as_view(),name='contact'),
 url(r'^Register',RegisterCustomer.as_view(),name='register'),
 url(r'^gall1',GallCreateView.as_view(),name='gall1'),
 url(r'^email',EmailView.as_view(),name='email'),
 url(r'^success',SuccessView.as_view(),name='success'),
 url(r'^gallist',GallistView.as_view(),name='gal1'),






]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

