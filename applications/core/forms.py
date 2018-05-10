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
