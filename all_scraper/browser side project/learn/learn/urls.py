"""learn URL Configuration

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
from django.conf.urls import url
from learn_app import views as learn_views   # new
from all_scraper import views as all_scraper_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^upload/queue$', learn_views.amazon, name='amazon'),
    # all_scraper
    url(r'^home/$', all_scraper_views.home, name='home'),
    url(r'^hello/$', all_scraper_views.hello, name='hello'),
    #
    url(r'^add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    #
    url(r'^add/$', learn_views.add, name='add'), # new
    #
    url(r'^$', learn_views.index),  # new

    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
