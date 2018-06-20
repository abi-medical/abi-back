from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin
from django import http
from django.contrib.auth import models as auth_models

from applications.authentication import (
    conf as authentication_conf
)

from . import (
    conf,
    models
)


class UserRolePermission(AccessMixin):
    model = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        else:
            if request.user.is_staff:
                return super(UserRolePermission, self).dispatch(request, *args, **kwargs)

            try:
                if self.model is None:
                    raise AssertionError("User role needs to define a model attribute")
                print("Getting object {} of class {}".format(request.user.id, self.model))
                print(self.model.objects.filter(pk=request.user.id))
                obj = self.model.objects.get(pk=request.user.id)
                print(obj)
                return super(UserRolePermission, self).dispatch(request, *args, **kwargs)
            except self.model.DoesNotExist:
                print("Object does not exists")
                pass
            messages.add_message(
                request,
                messages.ERROR,
                authentication_conf.PERMISSION_DENIED
            )
            return self.handle_no_permission()


class Administrator(UserRolePermission):
    model = models.Administrator

    def get_administrator(self):
        return models.Administrator.objects.get(pk=self.request.user.id)


class Specialist(UserRolePermission):
    model = models.Specialist

    def get_specialist(self):
        return models.Specialist.objects.get(pk=self.request.user.id)


class Patient(object):

    def get_patient(self):
        return models.Patient.objects.get(pk=self.kwargs.get("pk_patient", 0))


class Secretary(UserRolePermission):
    model = models.Secretary

    def get_secretary(self):
        return models.Secretary.objects.get(pk=self.request.user.id)


class AddPermissionsOnSave(object):
    permissions_to_add = []

    def form_valid(self, form=None):
        self.object = form.save()
        for permission_code_name in self.permissions_to_add:
            print(permission_code_name)
            try:
                for x in auth_models.Permission.objects.filter(codename=permission_code_name):
                    print(x.id, x.codename, x.content_type, x.name)
                self.object.user_permissions.add(auth_models.Permission.objects.get(codename=permission_code_name))
                self.object.save()
            except auth_models.Permission.DoesNotExist:
                pass
        return http.HttpResponseRedirect(self.get_success_url())


class Procedure(object):

    def get_procedure(self):
        return models.Procedure.objects.get(pk=self.kwargs.get("pk_procedure", 0))