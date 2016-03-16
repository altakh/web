from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'qa.views.new'),
    url(r'^login/$', 'qa.views.test'),
    url(r'^signup/$', 'qa.views.test'),
    url(r'^question/(?P<id>\d+)/$', 'qa.views.question'),
    url(r'^ask/$', 'qa.views.ask_add'),
    url(r'^popular/$', 'qa.views.popular'),
    url(r'^new/$', 'qa.views.test'),
    url(r'^answer/$', 'qa.views.answer_add'),
)
