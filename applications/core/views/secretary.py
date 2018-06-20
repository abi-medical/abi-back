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
    List all Secretarys
    """
    queryset = models.Secretary.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(
    mixins.Administrator,
    mixins.AddPermissionsOnSave,
    base_views.BaseCreateView
):
    """
    Create a Secretary
    """
    model = models.Secretary
    permission_required = (
        'core.add_secretary'
    )
    fields = None
    form_class = forms.Secretary
    permissions_to_add = [
        'add_patient',
        'add_procedure'
    ]

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.SECRETARY_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(mixins.Administrator, base_views.BaseDetailView):
    """
    Detail of a Secretary
    """
    model = models.Secretary

    def __init__(self):
        super(Detail, self).__init__()


class Update(mixins.Administrator, base_views.BaseUpdateView):
    """
    Update a Secretary
    """
    model = models.Secretary
    fields = None
    form_class = forms.Secretary
    permission_required = (
        'core.change_secretary'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.SECRETARY_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Secretary
    """
    model = models.Secretary
    permission_required = (
        'core.delete_secretary'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.SECRETARY_LIST_URL_NAME)
