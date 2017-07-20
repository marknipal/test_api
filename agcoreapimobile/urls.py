"""agcoreapimobile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
# from rest_framework import routers

# router = routers.DefaultRouter()

# router.register(r'groups',groups.GroupsViewSet,'groups')
# router.register(r'manufacturers',manufacturers.ManufacturersViewSet,'manufacturers')
# router.register(r'probes',probes.ProbesViewSet,'probes')
# router.register(r'sensor-types',sensor_types.Sensor_typesViewSet,'sensor-types')

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    # url(r'^/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]