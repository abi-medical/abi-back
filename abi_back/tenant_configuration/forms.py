from django import forms

from . import (
    models
)


class Tenant(forms.ModelForm):
    class Meta:
        model = models.Tenant
        fields = (
            'name',
        )

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-group"})
        }


