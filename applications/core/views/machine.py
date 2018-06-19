from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from base import views as base_views

from .base_view import BaseCreateView

from .. import (
    models,
    forms,
    conf,
    mixins
)


class List(mixins.Administrator, base_views.BaseListView):
    """
    List all Machines
    """
    queryset = models.Machine.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(mixins.Administrator, BaseCreateView):
    """
    Create a Machine
    """
    model = models.Machine
    fields = None
    form_class = forms.Machine

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINE_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(mixins.Administrator, base_views.BaseDetailView):
    """
    Detail of a Machine
    """
    model = models.Machine

    def __init__(self):
        super(Detail, self).__init__()


class Update(mixins.Administrator, base_views.BaseUpdateView):
    """
    Update a Machine
    """
    model = models.Machine
    fields = None
    form_class = forms.Machine

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINE_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(mixins.Administrator, base_views.BaseDeleteView):
    """
    Delete a Machine
    """
    model = models.Machine
    permission_required = (
        'core.delete_machine'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINE_LIST_URL_NAME)
