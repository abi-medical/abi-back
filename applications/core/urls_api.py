from rest_framework.routers import DefaultRouter
from . import (
    viewsets
)

api_urlpatterns = []

machineinput_router = DefaultRouter()

machineinput_router.register(
    r'^machineinput',
    viewsets.MachineInput,
    base_name="machineinput"
)

api_urlpatterns += machineinput_router.urls


urlpatterns = api_urlpatterns