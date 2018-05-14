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


class Patient(forms.ModelForm):

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
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-group'}),
            'description': forms.TextInput(attrs={'class': 'form-group'}),
            'type': forms.TextInput(attrs={'class': 'form-group'}),
            'code': forms.TextInput(attrs={'class': 'form-group'}),

        }
    def save(self, commit=True):
        machine = super(Machine, self).save(commit=False)
        if commit:
            machine.save()
        return machine