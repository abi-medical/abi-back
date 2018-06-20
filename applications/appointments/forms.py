from django import forms

from . import (
    models
)


class Appointment(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = (
            'patient_fk',
            'specialist_fk',
            'date'
        )


