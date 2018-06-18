from rest_framework import viewsets

from . import (
    serializers,
    models
)


class MachineInput(viewsets.ModelViewSet):
    
    serializer_class = serializers.MachineInput
    queryset = models.MachineInput.objects.all()

