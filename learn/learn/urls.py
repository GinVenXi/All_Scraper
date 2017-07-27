"""learn URL Configuration

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
from learn_app import views as learn_views

urlpatterns = [
    url(r'^home/$', learn_views.home, name='home'),

    url(r'^admin/', admin.site.urls),
    url(r'^index/$', learn_views.index, name='index'),

    url(r'^$', learn_views.login, name='login'),
    url(r'^login/$',learn_views.login,name = 'login'),
    url(r'^regist/$',learn_views.regist,name = 'regist'),
    url(r'^logout/$',learn_views.logout,name = 'logout'),
    url(r'^success/$',learn_views.indexs,name = 'success'),

    url(r'^sidebar/$', learn_views.sidebar, name = 'sidebar'),

    url(r'^page_test/$', learn_views.page_test, name='page_test'),
    url(r'^ajax_list/$', learn_views.ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', learn_views.ajax_dict, name='ajax-dict'),

    url(r'^hello/$', learn_views.hello, name='hello'),
]
