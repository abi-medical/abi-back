from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from base import views as base_views

from .. import (
    models,
    forms,
    conf,
    mixins
)


class List(mixins.Administrator, base_views.BaseListView):
    """
    List all Patients
    """
    queryset = models.Patient.objects.all()

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


class Detail(mixins.Administrator, base_views.BaseDetailView):
    """
    Detail of a Patient
    """
    model = models.Patient

    def __init__(self):
        super(Detail, self).__init__()


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
