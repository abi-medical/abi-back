from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django import http


from base import views as base_views
from .base_view import BaseCreateView

from applications.authentication import (
    mixins as authentication_mixins
)

from .. import (
    models,
    forms,
    conf,
    mixins
)


class List(authentication_mixins.SuperAdminRequiredMixin, base_views.BaseListView):
    """
    List all Administrators
    """
    queryset = models.Administrator.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(
    authentication_mixins.SuperAdminRequiredMixin,
    mixins.AddPermissionsOnSave,
    BaseCreateView,
):
    """
    Create a Administrator
    """
    model = models.Administrator
    fields = None
    form_class = forms.Administrator
    permissions_to_add = [
        'add_patient',
        'add_specialist'
    ]

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ADMINISTRATOR_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(authentication_mixins.SuperAdminRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Administrator
    """
    model = models.Administrator

    def __init__(self):
        super(Detail, self).__init__()


class Update(authentication_mixins.SuperAdminRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Administrator
    """
    model = models.Administrator
    fields = None
    form_class = forms.Administrator

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ADMINISTRATOR_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(authentication_mixins.SuperAdminRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Administrator
    """
    model = models.Administrator

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.ADMINISTRATOR_LIST_URL_NAME)
