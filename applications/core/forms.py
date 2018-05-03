from django import forms

from . import (
    models
)


class Administrator(forms.ModelForm):
    class Meta:
        model = models.Administrator
        fields = '__all__'


