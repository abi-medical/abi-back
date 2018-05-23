from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from base import views as base_views

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


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Procedure
    """
    model = models.Procedure

    def __init__(self):
        super(Detail, self).__init__()


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
