from rest_framework import serializers

from . import (
    models
)


class MachineInput(serializers.ModelSerializer):
    class Meta:
        model = models.MachineInput
        fields = (
            'machine_instance',
            'procedure',
            'content'
        )


