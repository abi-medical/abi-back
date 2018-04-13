from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Client(TenantMixin):
    # Taked from http://django-tenants.readthedocs.io/en/latest/install.html#the-tenant-domain-model
    name = models.CharField(max_length=100)
    paid_until = models.DateField(null=True, default=None)
    on_trial = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    # Also taked from # Taked from http://django-tenants.readthedocs.io/en/latest/install.html#the-tenant-domain-model
    pass