from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django import http

from base import views as base_views

from .. import (
    models,
    forms,
    conf,
    mixins
)


from . import (
    procedure
)


class List(PermissionRequiredMixin, base_views.BaseListView):
    """
    List all Patients
    """
    queryset = models.Patient.objects.all()
    permission_required = [
        'core.add_patient'
    ]

    def __init__(self):
        super(List, self).__init__()


class Create(mixins.Administrator, base_views.BaseCreateView):
    """
    Create a Patient
    """
    model = models.Patient
    fields = None
    form_class = forms.Patient

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PATIENT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(PermissionRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Patient
    """
    model = models.Patient
    template_name = "core/patient/detail.html"
    permission_required = [
        'core.add_patient'
    ]

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        context['add_procedure_reverse_url'] = self.get_add_procedure_reverse_url()

        context['procedures'] = models.Procedure.objects.filter(patient_fk=self.get_object())

        return context

    def get_add_procedure_reverse_url(self):
        return reverse_lazy(
            conf.PATIENT_ADD_PROCEDURE_URL_NAME,
            kwargs={
                "pk_patient": self.get_object().id
            }
        )


class Update(mixins.Administrator, base_views.BaseUpdateView):
    """
    Update a Patient
    """
    model = models.Patient
    fields = None
    form_class = forms.Patient

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PATIENT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(mixins.Administrator, base_views.BaseDeleteView):
    """
    Delete a Patient
    """
    model = models.Patient
    permission_required = (
        'core.delete_patient'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PATIENT_LIST_URL_NAME)


class AddProcedure(
    mixins.Specialist,
    mixins.Patient,
    procedure.Create
):
    fields = None
    form_class = forms.ProcedureNoPatientNoSpecialist

    def form_valid(self, form):
        procedure_object = form.save(commit=False)
        procedure_object.specialist_fk = self.get_specialist()
        procedure_object.patient_fk = self.get_patient()
        procedure_object.save()
        return http.HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            conf.PATIENT_DETAIL_URL_NAME,
            kwargs={
                'pk':self.get_patient().id
            }
        )