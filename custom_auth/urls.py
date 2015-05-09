from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^test/', TemplateView.as_view(template_name="base_site.html")),
#    url(r'^admin/', include(admin.site.urls)),
]