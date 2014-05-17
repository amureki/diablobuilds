from django.conf.urls import patterns, url
from project.apps.core.views import BuildsList, BuildDetail, BuildAdd, IndexPage, BuildVote, FAQPage


urlpatterns = patterns(
    'core.views',
    url(r'^$', IndexPage.as_view(), name='index'),
    url(r'^list/$', BuildsList.as_view(), {}, name='builds_list'),
    url(r'^list/(?P<optional>.*)/$', BuildsList.as_view(), {}, name='builds_list'),
    url(r'^(?P<pk>\d+)/$', BuildDetail.as_view(), name='build_detail'),
    url(r'^vote/$', BuildVote.as_view(), name='build_vote'),
    url(r'^add/$', BuildAdd.as_view(), name='build_add'),

    url(r'^faq/$', FAQPage.as_view(), name='faq'),

)