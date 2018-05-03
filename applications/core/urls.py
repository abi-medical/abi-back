from django.conf.urls import url

from . import conf

urlpatterns = []

from .views import administrator

urlpatterns += [
    # administrator
    url(
        '^administrator/$',
        administrator.List.as_view(),
        name=conf.ADMINISTRATOR_LIST_URL_NAME
    ),
    url(
        '^administrator/create/$',
        administrator.Create.as_view(),
        name=conf.ADMINISTRATOR_CREATE_URL_NAME
    ),
    url(
        '^administrator/(?P<pk>\d+)/$',
        administrator.Detail.as_view(),
        name=conf.ADMINISTRATOR_DETAIL_URL_NAME
    ),
    url(
        '^administrator/(?P<pk>\d+)/update/$',
        administrator.Update.as_view(),
        name=conf.ADMINISTRATOR_UPDATE_URL_NAME
    ),
    url(
        '^administrator/(?P<pk>\d+)/delete/$',
        administrator.Delete.as_view(),
        name=conf.ADMINISTRATOR_DELETE_URL_NAME
    ),
]

