from django.conf.urls import url
from django.contrib import admin

from . import conf

urlpatterns = [
    url(
        r'^admin/', admin.site.urls
    ),
    url(
        r'^authentication/',
        (
            "applications.authentication.urls",
            "authentication",
            ""
        )
    ),
]

from .views import tenant

urlpatterns += [
    # tenant
    url(
        '^tenant/$',
        tenant.List.as_view(),
        name=conf.TENANT_LIST_URL_NAME
    ),
    url(
        '^tenant/create/$',
        tenant.Create.as_view(),
        name=conf.TENANT_CREATE_URL_NAME
    ),
    url(
        '^tenant/(?P<pk>\d+)/$',
        tenant.Detail.as_view(),
        name=conf.TENANT_DETAIL_URL_NAME
    ),
    url(
        '^tenant/(?P<pk>\d+)/update/$',
        tenant.Update.as_view(),
        name=conf.TENANT_UPDATE_URL_NAME
    ),
    url(
        '^tenant/(?P<pk>\d+)/delete/$',
        tenant.Delete.as_view(),
        name=conf.TENANT_DELETE_URL_NAME
    ),
]

