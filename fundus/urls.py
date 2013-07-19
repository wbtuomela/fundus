from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    url(r'^contact/', include('dico.urls')),
    url(r'^nimda/', include(admin.site.urls)),
)
