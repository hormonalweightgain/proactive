from django.contrib import admin
from main.models import Patient

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=['name','email','dob','weight','waist','hip','purpose','have_baby','hyperprolactinemia','pcos_pcod','hypothyroidism','other','hyperprolactinemia_days','pcos_pcod_days','hypothyroidism_days','other_days','symptoms7','month8','year8','weight9','time9','time9_d']

admin.site.register(
    Patient,
    PatientAdmin,
)
