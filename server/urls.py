"""ElectricalCheckIn URL Configuration

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
"""from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]"""

"""from rest_framework.routers import DefaultRouter
from billmng.views import UserViewSet,BillViewSet

router = DefaultRouter()
router.register(prefix='users', viewset=UserViewSet)
router.register(prefix='bills', viewset=BillViewSet)

urlpatterns = router.urls"""

from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from django.contrib import admin

from billmng.views import UserViewSet, BillViewSet, UserBillsList, UserList, BillPostList
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'users',UserViewSet)
router.register(r'bills',BillViewSet)


urlpatterns = patterns('',
       url(r'^', include(router.urls)),
       url(r'^main/addbill$', 'billmng.views.add_bill'),
       url(r'^main/bills/([0-9a-zA-Z]{0,20})$', 'billmng.views.deleteBill'),
       url(r'^main/$','billmng.views.mainPage'),
       url(r'^main/users$','billmng.views.usersInfo'),
       url(r'^main/users/([0-9]{9}[a-zA-Z]{1})$','billmng.views.singleUserDetails'),
       url(r'^main/bills$','billmng.views.billsInfo'),
       url(r'^main/chart$', 'billmng.views.chart'),
       url(r'^userbills/(?P<idcard>[0-9]{9}[a-zA-Z]{1})$', UserBillsList.as_view()),
       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
       url(r'^admin/', include(admin.site.urls)),
)

"""class RenderizeView(TemplateView):
    def get_template_names(self):
        test = self.kwargs.get('template_name')
        return [self.kwargs.get('template_name') + ".html"]


user_urls = patterns('',
    url(r'^/$', UserViewSet.as_view({'get': 'list'}), name='users-view'),
    url(r'^list/$', UserList.as_view(), name='user-list-view'),
)

bills_urls = patterns('',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', BillPostList.as_view(), name='bills-by-user'),
    url(r'^/$', BillViewSet.as_view({'get': 'list'}), name='bills-view')
)
urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/users',include(user_urls)),
    url(r'^api/bills',include(bills_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<template_name>\w+)$', RenderizeView.as_view(), name='main-view'),
    url(r'^$', TemplateView.as_view(template_name='base.html'))
)"""




