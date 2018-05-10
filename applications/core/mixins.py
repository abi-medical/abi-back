from django.contrib import messages
from django.contrib.auth.mixins import AccessMixin

from applications.authentication import (
    conf as authentication_conf
)

from . import (
    conf,
    models
)


class Administrator(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        else:
            if request.user.is_staff:
                return super(Administrator, self).dispatch(request, *args, **kwargs)

            try:
                models.Administrator.objects.get(pk=request.user.id)
                return super(Administrator, self).dispatch(request, *args, **kwargs)
            except models.Administrator.DoesNotExist:
                pass
            messages.add_message(
                request,
                messages.ERROR,
                authentication_conf.PERMISSION_DENIED
            )
            return self.handle_no_permission()


