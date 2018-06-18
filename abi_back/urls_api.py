from django.conf.urls import url

from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import IsAdminUser


urlpatterns = []

urlpatterns += [
    url(
        r'^docs/',
        include_docs_urls(
            permission_classes=(IsAdminUser,)
        )
    ),
    url(
        r'^core/',
        (
            "applications.core.urls_api",
            "core_api",
            "core_api"
        )

    ),
]
