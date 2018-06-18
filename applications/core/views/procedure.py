from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import edit
from django import http

from base import views as base_views

from . import (
    machine_instance
)

from .. import (
    models,
    forms,
    conf
)


class List(LoginRequiredMixin, base_views.BaseListView):
    """
    List all Procedures
    """
    queryset = models.Procedure.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Procedure
    """
    model = models.Procedure
    permission_required = (
        'core.add_procedure'
    )
    fields = '__all__'

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PROCEDURE_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(LoginRequiredMixin, base_views.BaseDetailView, edit.ProcessFormView, edit.FormMixin):
    """
    Detail of a Procedure
    """
    template_name = "core/procedure/detail.html"
    model = models.Procedure
    form_class = forms.SimpleObservation

    def __init__(self):
        super(Detail, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        context['observations'] = models.Observation.objects.filter(
            procedure=self.get_object()
        )

        context['machines'] = models.MachineInstance.objects.filter(
            machine=self.get_object().treatment_fk.machine
        )

        for machine in context['machines']:
            machine.activate_url_reverse = reverse_lazy(
                conf.PROCEDURE_ACTIVATE_MACHINE_URL_NAME,
                kwargs={
                    'pk_procedure': self.get_object().id,
                    'pk': machine.id
                }
            )

        return context

    def form_valid(self, form):
        observation = form.save(commit=False)
        observation.procedure = self.get_object()
        observation.specialist_fk = models.Specialist.objects.get(pk=self.request.user.id)
        observation.save()
        return http.HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            conf.PROCEDURE_DETAIL_URL_NAME,
            kwargs={
                'pk': self.get_object().id
            }
        )


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Procedure
    """
    model = models.Procedure
    fields = '__all__'
    permission_required = (
        'core.change_procedure'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PROCEDURE_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Procedure
    """
    model = models.Procedure
    permission_required = (
        'core.delete_procedure'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.PROCEDURE_LIST_URL_NAME)


class Activate(machine_instance.Activate):

    def dispatch(self, request, *args, **kwargs):
        print("Before calling super")
        p = super(Activate, self).dispatch(request, *args, **kwargs)
        print(p)
        return p
