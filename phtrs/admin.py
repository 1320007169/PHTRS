from django.contrib import admin
from .models import Worker, Citizen
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Worker, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Citizen, PatientAdmin)



