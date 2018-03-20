from django.conf.urls import  url
from . import views
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^detail/$', views.detail),
    url(r'^list/$', views.list),
    # url(r'^register_exist/$', views.register_exist),
    # url(r'^user_login_handle/$', views.user_login_handle),
    # url(r'^user_center_info/$', views.user_center_info),
    # url(r'^user_center_order/$', views.user_center_order),
    # url(r'^user_center_site/$', views.user_center_site),
    # url(r'^user_site_handle/$', views.user_site_handle)

]