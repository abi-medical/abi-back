import requests

from django.core.urlresolvers import reverse_lazy

from base import views as base_views

from .. import (
    models,
    forms,
    conf,
    mixins
)


class List(mixins.Administrator, base_views.BaseListView):
    """
    List all MachineInstances
    """
    queryset = models.MachineInstance.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(mixins.Administrator, base_views.BaseCreateView):
    """
    Create a MachineInstance
    """
    model = models.MachineInstance
    fields = '__all__'

    def __init__(self):
        super(Create, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINEINSTANCE_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(mixins.Administrator, base_views.BaseDetailView):
    """
    Detail of a MachineInstance
    """
    model = models.MachineInstance

    def __init__(self):
        super(Detail, self).__init__()


class Update(mixins.Administrator, base_views.BaseUpdateView):
    """
    Update a MachineInstance
    """
    model = models.MachineInstance
    fields = '__all__'

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINEINSTANCE_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(mixins.Administrator, base_views.BaseDeleteView):
    """
    Delete a MachineInstance
    """
    model = models.MachineInstance

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.MACHINEINSTANCE_LIST_URL_NAME)


class Activate(
    # mixins.Specialist,
    Detail
):
    template_name = "core/machine_instance/activation.html"

    def get_context_data(self, **kwargs):
        context = super(Activate, self).get_context_data(**kwargs)

        response = requests.get(self.get_object().activation_url)

        context['activation_status'] = conf.MACHINEINSTANCE_ACTIVATED_MESSAGE \
            if response.status_code == 200 \
            else \
            conf.MACHINEINSTANCE_UNACTIVATED_MESSAGE

        return context
