from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from spider import views

urlpatterns = [
    url(r'^vjudge^', views.get_vjudge_info),
    url(r'^testvjudge', views.testvjudge),
    url(r'^vjudgebind', views.vjudgebind),
    url(r'^getList', views.getList),
    url(r'^getTreeList', views.getListTree)
]
