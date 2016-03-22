from django.conf.urls import include, url
from django.contrib import admin
from base import views


urlpatterns = [
    url(r'^courses', views.courses_view, name='course_view'),
    url(r'^help', views.user_help, name='user_help'),
    url(r'^history', views.pos_history, name='pos_history'),
    url(r'^home', views.home, name='home'),
    url(r'^manage', views.user_manage, name='user_manage'),
    url(r'^new', views.pos_new, name='pos_new'),
    url(r'^register', views.register, name='register'),
    url(r'^user', views.user_detail, name='user_detail'),
    url(r'^user/(?P<id>\d+)/', views.user_detail, name='user_detail'),
    url(r'^view', views.pos_view, name='pos_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^$', views.index, name='index'),
]
