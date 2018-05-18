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

from .views import specialist

urlpatterns += [
    # specialist
    url(
        '^specialist/$',
        specialist.List.as_view(),
        name=conf.SPECIALIST_LIST_URL_NAME
    ),
    url(
        '^specialist/create/$',
        specialist.Create.as_view(),
        name=conf.SPECIALIST_CREATE_URL_NAME
    ),
    url(
        '^specialist/patients/$',
        specialist.ListWithPatients.as_view(),
        name=conf.SPECIALIST_WITH_PATIENTS_URL_NAME
    ),
    url(
        '^specialist/(?P<pk>\d+)/$',
        specialist.Detail.as_view(),
        name=conf.SPECIALIST_DETAIL_URL_NAME
    ),
    url(
        '^specialist/(?P<pk>\d+)/update/$',
        specialist.Update.as_view(),
        name=conf.SPECIALIST_UPDATE_URL_NAME
    ),
    url(
        '^specialist/(?P<pk>\d+)/delete/$',
        specialist.Delete.as_view(),
        name=conf.SPECIALIST_DELETE_URL_NAME
    ),
]

from .views import patient

urlpatterns += [
    # patient
    url(
        '^patient/$',
        patient.List.as_view(),
        name=conf.PATIENT_LIST_URL_NAME
    ),
    url(
        '^patient/create/$',
        patient.Create.as_view(),
        name=conf.PATIENT_CREATE_URL_NAME
    ),
    url(
        '^patient/(?P<pk>\d+)/$',
        patient.Detail.as_view(),
        name=conf.PATIENT_DETAIL_URL_NAME
    ),
    url(
        '^patient/(?P<pk>\d+)/update/$',
        patient.Update.as_view(),
        name=conf.PATIENT_UPDATE_URL_NAME
    ),
    url(
        '^patient/(?P<pk>\d+)/delete/$',
        patient.Delete.as_view(),
        name=conf.PATIENT_DELETE_URL_NAME
    ),
]

from .views import machine

urlpatterns += [
    # machine
    url(
        '^machine/$',
        machine.List.as_view(),
        name=conf.MACHINE_LIST_URL_NAME
    ),
    url(
        '^machine/create/$',
        machine.Create.as_view(),
        name=conf.MACHINE_CREATE_URL_NAME
    ),
    url(
        '^machine/(?P<pk>\d+)/$',
        machine.Detail.as_view(),
        name=conf.MACHINE_DETAIL_URL_NAME
    ),
    url(
        '^machine/(?P<pk>\d+)/update/$',
        machine.Update.as_view(),
        name=conf.MACHINE_UPDATE_URL_NAME
    ),
    url(
        '^machine/(?P<pk>\d+)/delete/$',
        machine.Delete.as_view(),
        name=conf.MACHINE_DELETE_URL_NAME
    ),
]


