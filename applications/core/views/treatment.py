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
    List all Treatments
    """
    queryset = models.Treatment.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(mixins.Administrator, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Treatment
    """
    model = models.Treatment
    permission_required = (
        'core.add_treatment'
    )
    fields = '__all__'

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.TREATMENT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(mixins.Administrator, base_views.BaseDetailView):
    """
    Detail of a Treatment
    """
    model = models.Treatment

    def __init__(self):
        super(Detail, self).__init__()


class Update(mixins.Administrator, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Treatment
    """
    model = models.Treatment
    fields = '__all__'
    permission_required = (
        'core.change_treatment'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.TREATMENT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(mixins.Administrator, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Treatment
    """
    model = models.Treatment
    permission_required = (
        'core.delete_treatment'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.TREATMENT_LIST_URL_NAME)
