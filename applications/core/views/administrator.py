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
    List all Administrators
    """
    queryset = models.Administrator.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Administrator
    """
    model = models.Administrator
    permission_required = (
        '..add_administrator'
    )
    fields = '__all__'

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ADMINISTRATOR_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(LoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Administrator
    """
    model = models.Administrator

    def __init__(self):
        super(Detail, self).__init__()


class Update(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Administrator
    """
    model = models.Administrator
    fields = '__all__'
    permission_required = (
        '..change_administrator'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ADMINISTRATOR_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(LoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Administrator
    """
    model = models.Administrator
    permission_required = (
        '..delete_administrator'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ADMINISTRATOR_LIST_URL_NAME)
