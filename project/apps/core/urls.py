from django.conf.urls import patterns, url
from project.apps.core.views import BuildsList, BuildDetail, BuildAdd, IndexPage, BuildChangeRating


urlpatterns = patterns(
    'core.views',
    url(r'^$', IndexPage.as_view(), name='index'),
    url(r'^list/$', BuildsList.as_view(), name='builds_list'),
    url(r'^(?P<pk>\d+)/$', BuildDetail.as_view(), name='build_detail'),
    url(r'^rating/$', BuildChangeRating.as_view(), name='build_change_rating'),
    url(r'^add/$', BuildAdd.as_view(), name='build_add'),

)