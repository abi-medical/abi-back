from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from base import views as base_views
from .base_view import BaseCreateView,BaseUpdateView,BaseDeleteView
from .. import (
    models,
    forms,
    conf,
    mixins
)


class List(mixins.Administrator, base_views.BaseListView):
    """
    List all Specialists
    """
    template_name = "core/specialist/list.html"
    queryset = models.Specialist.objects.all()

    def __init__(self):
        super(List, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(List, self).get_context_data(**kwargs)

        context['report_with_patients_url_reversed'] = reverse_lazy(
            conf.SPECIALIST_WITH_PATIENTS_URL_NAME
        )

        return context


class Create(
    mixins.Administrator,
    mixins.AddPermissionsOnSave,
    BaseCreateView,
):
    """
    Create a Specialist
    """
    model = models.Specialist
    fields = None
    form_class = forms.Specialist
    permissions_to_add = [
        'add_patient',
        'add_procedure'
    ]

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.SPECIALIST_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(mixins.Administrator, base_views.BaseDetailView):
    """
    Detail of a Specialist
    """
    model = models.Specialist

    def __init__(self):
        super(Detail, self).__init__()


class Update(mixins.Administrator, BaseUpdateView):
    """
    Update a Specialist
    """
    model = models.Specialist
    fields = None
    form_class = forms.Specialist

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.SPECIALIST_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(mixins.Administrator, BaseDeleteView):
    """
    Delete a Specialist
    """
    model = models.Specialist
    permission_required = (
        'core.delete_specialist'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.SPECIALIST_LIST_URL_NAME)


class ListWithPatients(List):
    template_name = "core/specialist/list_with_patients.html"

    def get_context_data(self, **kwargs):
        context = super(ListWithPatients, self).get_context_data(**kwargs)

        for specialist in context[self.context_object_name]:
            specialist.patients = models.Patient.objects.filter(specialist_fk=specialist)

        return context

