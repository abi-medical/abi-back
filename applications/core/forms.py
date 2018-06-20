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
            'username': forms.TextInput(attrs={'class': 'form-control  col-md-7 col-xs-12'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control  col-md-7 col-xs-12'})
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
            'name': forms.TextInput(attrs={'class': 'form-control  col-md-7 col-xs-12'}),
            'description': forms.TextInput(attrs={'class': 'form-control  col-md-7 col-xs-12'}),
            'type': forms.TextInput(attrs={'class': 'form-control  col-md-7 col-xs-12'}),
            'code': forms.TextInput(attrs={'class': 'form-control  col-md-7 col-xs-12'}),
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
class MachineInstance(forms.ModelForm):
    class Meta:
        model = models.MachineInstance
        fields = '__all__'


class MachineInput(forms.ModelForm):
    class Meta:
        model = models.MachineInput
        fields = '__all__'


class MachineInput(forms.ModelForm):
    class Meta:
        model = models.MachineInput
        fields = '__all__'


