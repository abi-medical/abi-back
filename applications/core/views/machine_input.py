from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from base import views as base_views
from .base_view import BaseCreateView,BaseUpdateView
from .. import (
    models,
    forms,
    conf
)


class List(LoginRequiredMixin, base_views.BaseListView):
    """
    List all MachineInputs
    """
    queryset = models.MachineInput.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(LoginRequiredMixin, PermissionRequiredMixin, BaseCreateView):
    """
    Create a MachineInput
    """
    model = models.MachineInput
    permission_required = (
        'core.add_machineinput'
    )
    fields = '__all__'

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINEINPUT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a MachineInput
    """
    model = models.MachineInput

    def __init__(self):
        super(Detail, self).__init__()


class Update(LoginRequiredMixin, PermissionRequiredMixin, BaseUpdateView):
    """
    Update a MachineInput
    """
    model = models.MachineInput
    fields = '__all__'
    permission_required = (
        'core.change_machineinput'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINEINPUT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a MachineInput
    """
    model = models.MachineInput
    permission_required = (
        'core.delete_machineinput'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINEINPUT_LIST_URL_NAME)
