from django.conf.urls import include, url
from django.contrib import admin
from base import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home', views.home, name='home'),
    url(r'^courses', views.courses_view, name='course_view'),
    url(r'^user/(?P<id>\d+)/', views.user_detail, name='user_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
