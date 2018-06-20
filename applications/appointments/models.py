from django.db import models

from base import models as base_models

from applications.core import (
    models as core_models
)

from . import (
    conf
)

# Create your models here.


class Appointment(base_models.FullSlugBaseModel):
    patient_fk = models.ForeignKey(core_models.Patient)
    specialist_fk = models.ForeignKey(core_models.Specialist)
    secretary_fk = models.ForeignKey(core_models.Secretary)
    date = models.DateTimeField()

    url_name = conf.APPOINTMENT_DETAIL_URL_NAME

    def __init__(self, *args, **kwargs):
        super(Appointment, self).__init__(*args, *kwargs)

    def __str__(self):
        return "{} {} {}".format(str(self.patient_fk), str(self.specialist_fk), str(self.date))
