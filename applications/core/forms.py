from django import forms

from . import (
    models
)


class Administrator(forms.ModelForm):
    class Meta:
        model = models.Administrator
        fields = [
            'username',
            'password'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-group'}),
            'password': forms.PasswordInput(attrs={'class': 'form-group'})
        }

    def save(self, commit=True):
        """
        Custom save method for determine active and unactive users
        :param commit:
        :return:
        """
        user = super(Administrator, self).save(commit=False)
        if commit:
            user.is_active = True
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user


class Specialist(Administrator):

    class Meta(Administrator.Meta):
        model = models.Specialist


class Patient(Administrator):

    class Meta(Administrator.Meta):
        model = models.Patient
        fields = [
            'username',
            'password',
            'specialist_fk'
        ]


class Machine(forms.ModelForm):
    class Meta:
        model = models.Machine
        fields = [
            'name',
            'description',
            'type',
            'code'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-group'}),
            'description': forms.TextInput(attrs={'class': 'form-group'}),
            'type': forms.TextInput(attrs={'class': 'form-group'}),
            'code': forms.TextInput(attrs={'class': 'form-group'}),
        }


class Treatment(forms.ModelForm):
    class Meta:
        model = models.Treatment
        fields = '__all__'


class Procedure(forms.ModelForm):
    class Meta:
        model = models.Procedure
        fields = '__all__'


class ProcedureNoPatientNoSpecialist(forms.ModelForm):
    class Meta:
        model = models.Procedure
        fields = [
            'treatment_fk',
            'action'
        ]


class SimpleObservation(forms.ModelForm):
    class Meta:
        model = models.Observation
        fields = [
            'observation',
        ]
