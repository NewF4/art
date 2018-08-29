"""arts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.core.paginator import Paginator
from django.shortcuts import render

import  xadmin as admin
from art.models import Category,Art
def index(request):
    cates = Category.objects.filter(parent=True)
    arts = Art.objects.all()
    paginator = Paginator
    return render(request,'index.html',locals())
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
     url(r'^admin/', admin.site.urls),
     url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^index/',index)
]
