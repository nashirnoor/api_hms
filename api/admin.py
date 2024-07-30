from django.contrib import admin

from .models import User, Department, Doctor, Patient, PatientRecord

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(PatientRecord)