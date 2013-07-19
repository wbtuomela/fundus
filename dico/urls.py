from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import ContactFormView

urlpatterns = patterns(
    '',
    url(r'^us/$',
        ContactFormView.as_view(),
        name='contact'),
    url(r'^sent/$',
        TemplateView.as_view(template_name='sent.html'),
        name='sent'),
)
