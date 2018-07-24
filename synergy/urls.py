"""synergy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.views.generic import TemplateView
import application.views as views

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^demands/$', TemplateView.as_view(template_name='demands.html')),
    url(r'^payment/$', TemplateView.as_view(template_name='payment.html')),

    url(r'^archive/$', views.MagazineListView.as_view()),
    url(r'^archive/(?P<magazine>\d+)/$', views.MagazineView.as_view()),
    url(r'^archive/article(?P<pagename>\w+)$', views.ArticleView.as_view()),

    url(r'^feedback/$', views.FeedbackView.as_view()),


    url(r'^admin/', admin.site.urls),

    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),



]
