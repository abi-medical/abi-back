from django.contrib import admin


from . import models
# Register your models here.
admin.site.register(models.Tenant)
admin.site.register(models.Domain)

