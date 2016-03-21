from django.conf.urls import include, url
from django.contrib import admin
from cypos.base import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<id>\d+)/', views.user_detail, name='user_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
