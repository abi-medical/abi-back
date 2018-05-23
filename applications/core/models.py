from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.


from . import (
    conf
)


class Administrator(auth_models.User):

    url_name = conf.ADMINISTRATOR_DETAIL_URL_NAME

    def __init__(self, *args, **kwargs):
        super(Administrator, self).__init__(*args, *kwargs)


class Specialist(auth_models.User):

    url_name = conf.SPECIALIST_DETAIL_URL_NAME

    def __init__(self, *args, **kwargs):
        super(Specialist, self).__init__(*args, *kwargs)


class Patient(auth_models.User):

    url_name = conf.PATIENT_DETAIL_URL_NAME

    specialist_fk = models.ForeignKey(Specialist)

    def __init__(self, *args, **kwargs):
        super(Patient, self).__init__(*args, *kwargs)


class PatientAssignHistory(models.Model):
    patient_fk = models.ForeignKey(Patient)
    specialist_fk = models.ForeignKey(Specialist)
    assigner_fk = models.ForeignKey(Administrator)
    created = models.DateTimeField(auto_now_add=True)


class Machine(models.Model):

    name = models.TextField()
    description = models.TextField()
    type = models.TextField()
    code = models.TextField()

    url_name = conf.MACHINE_DETAIL_URL_NAME

    def __init__(self, *args, **kwargs):
        super(Machine, self).__init__(*args, *kwargs)

    def __str__(self):
        return self.name


class Treatment(models.Model):
    name = models.TextField()
    description = models.TextField()
    machine = models.ForeignKey(Machine, null=True, blank=True)

    url_name = conf.TREATMENT_DETAIL_URL_NAME

    def __str__(self):
        return self.name


class Procedure(models.Model):
    patient_fk = models.ForeignKey(Patient)
    specialist_fk = models.ForeignKey(Specialist)
    treatment_fk = models.ForeignKey(Treatment, null=True)
    action = models.TextField()

    url_name = conf.PROCEDURE_DETAIL_URL_NAME

    def __str__(self):
        return "{} {} {}".format(self.patient_fk, self.specialist_fk, self.treatment_fk)


class Observation(models.Model):
    specialist_fk = models.ForeignKey(Specialist)
    procedure = models.ForeignKey(Procedure)
    observation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
