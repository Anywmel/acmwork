from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from users import views

urlpatterns = [
    url(r'^info', views.get_user_info),
    url(r'^login', obtain_jwt_token),
    url(r'^logout', views.logout),
    url(r'^register', views.register),
    url(r'^saveUserInfo',views.save_user_info)
]
