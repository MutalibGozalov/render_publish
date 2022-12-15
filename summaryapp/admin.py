from django.contrib import admin
from summaryapp.models import ServiceModel, AssingmentModel, BarberModel
from django.contrib.auth.admin import  UserAdmin

# Register your models here.
admin.site.register(ServiceModel)
admin.site.register(AssingmentModel)
admin.site.register(BarberModel)