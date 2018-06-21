from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django import http

from base import views as base_views

from applications.core import (
    mixins as core_mixins,
    models as core_models
)

from .. import (
    models,
    forms,
    conf
)


class List(LoginRequiredMixin, base_views.BaseListView):
    """
    List all Appointments
    """
    queryset = models.Appointment.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(
    core_mixins.Secretary,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    base_views.BaseCreateView
):
    """
    Create a Appointment
    """
    model = models.Appointment
    permission_required = (
        'appointments.add_appointment'
    )
    fields = None
    form_class = forms.Appointment

    def __init__(self):
        super(Create, self).__init__()

    def form_valid(self, form):
        appointment = form.save(commit=False)
        try:
            appointment.secretary_fk = self.get_secretary()
        except core_models.Secretary.DoesNotExist:
            appointment.secretary_fk = core_models.Secretary.objects.all()[0]
        appointment.save()

        return http.HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse_lazy(conf.APPOINTMENT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Appointment
    """
    model = models.Appointment

    def __init__(self):
        super(Detail, self).__init__()


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Appointment
    """
    model = models.Appointment
    fields = None
    form_class = forms.Appointment
    permission_required = (
        'appointments.change_appointment'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.APPOINTMENT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Appointment
    """
    model = models.Appointment
    permission_required = (
        'appointments.delete_appointment'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.APPOINTMENT_LIST_URL_NAME)
