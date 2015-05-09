from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [    
    url(r'^login/', 'django.contrib.auth.views.login',
     {'template_name':'custom_auth/login.html'}, name = 'login'),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name = 'logout'),
]