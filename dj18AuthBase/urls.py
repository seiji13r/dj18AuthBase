from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'dj18AuthBase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^custom_auth/', include('custom_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]