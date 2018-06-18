from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.text import slugify
from django.conf import LazySettings
from django import http

from applications.authentication.mixins import CustomLoginRequiredMixin

from base import views as base_views

from .. import (
    models,
    forms,
    conf,
    route_53_utils
)


settings = LazySettings()


class List(CustomLoginRequiredMixin, base_views.BaseListView):
    """
    List all Tenants
    """
    queryset = models.Tenant.objects.all()

    def __init__(self):
        super(List, self).__init__()


class Create(CustomLoginRequiredMixin, PermissionRequiredMixin, base_views.BaseCreateView):
    """
    Create a Tenant
    """
    model = models.Tenant
    permission_required = (
        'tenant_configuration.add_tenant'
    )
    fields = None
    form_class = forms.Tenant

    def __init__(self):
        super(Create, self).__init__()

    def form_valid(self, form):
        tenant = form.save(commit=False)
        tenant.schema_name = slugify(tenant.name)
        tenant.save()

        self.object = tenant

        models.Domain.objects.create(
            domain="{}.{}".format(tenant.schema_name, settings.MAIN_HOST),
            tenant=tenant
        )

        if settings.ABI_REGISTER_ROUTE_53:
            route_53_utils.insert_record(
                settings.AWS_ROUTE_53_ACCESS_KEY_ID,
                settings.AWS_ROUTE_53_SECRET_ACCESS_KEY,
                tenant.schema_name,
                settings.AWS_ROUTE_53_DEFAULT_TENANT_IP,
                settings.AWS_ROUTE_53_HOSTED_ZONE_ID
            )
        return http.HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(conf.TENANT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Detail(CustomLoginRequiredMixin, base_views.BaseDetailView):
    """
    Detail of a Tenant
    """
    model = models.Tenant

    def __init__(self):
        super(Detail, self).__init__()


class Update(CustomLoginRequiredMixin, PermissionRequiredMixin, base_views.BaseUpdateView):
    """
    Update a Tenant
    """
    model = models.Tenant
    fields = '__all__'
    permission_required = (
        'tenant_configuration.change_tenant'
    )

    def __init__(self):
        super(Update, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.TENANT_DETAIL_URL_NAME, kwargs={
            'pk': self.object.id
        })


class Delete(CustomLoginRequiredMixin, PermissionRequiredMixin, base_views.BaseDeleteView):
    """
    Delete a Tenant
    """
    model = models.Tenant
    permission_required = (
        'tenant_configuration.delete_tenant'
    )

    def __init__(self):
        super(Delete, self).__init__()

    def get_success_url(self):
        return reverse_lazy(conf.TENANT_LIST_URL_NAME)
