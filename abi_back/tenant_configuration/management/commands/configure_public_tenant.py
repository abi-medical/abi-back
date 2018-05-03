from django.core.management.base import BaseCommand
from django.conf import LazySettings
from abi_back.tenant_configuration import models, conf

settings = LazySettings()


class Command(BaseCommand):
    help = conf.messages.CONFIGURE_PUBLIC_TENANT

    def handle(self, *args, **options):
        main_tenant = models.Tenant.objects.create(
            schema_name='public',
            name='Main Schema',
        )
        main_domain = models.Domain.objects.create(
            domain=settings.MAIN_HOST,
            tenant=main_tenant
        )

        print(conf.messages.MAIN_DOMAIN_CREATED.format(main_domain.domain))
