from django.conf.urls import include, url

urlpatterns = [
    url(r'^cart/', include('df_cart.urls', namespace='cart'))

]