from django.conf.urls import url

from . import conf

urlpatterns = [

]

from .views import appointment

urlpatterns += [
    # appointment
    url(
        '^appointment/$',
        appointment.List.as_view(),
        name=conf.APPOINTMENT_LIST_URL_NAME
    ),
    url(
        '^appointment/create/$',
        appointment.Create.as_view(),
        name=conf.APPOINTMENT_CREATE_URL_NAME
    ),
    url(
        '^appointment/(?P<pk>\d+)/$',
        appointment.Detail.as_view(),
        name=conf.APPOINTMENT_DETAIL_URL_NAME
    ),
    url(
        '^appointment/(?P<pk>\d+)/update/$',
        appointment.Update.as_view(),
        name=conf.APPOINTMENT_UPDATE_URL_NAME
    ),
    url(
        '^appointment/(?P<pk>\d+)/delete/$',
        appointment.Delete.as_view(),
        name=conf.APPOINTMENT_DELETE_URL_NAME
    ),
]

