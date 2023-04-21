from django.contrib import admin
from .models import Complaint,Grievance

class CAdmin(admin.ModelAdmin):
    list_display = ('user','Subject','Type_of_complaint','Description','Time','status')

admin.site.register(Complaint,CAdmin)
admin.site.register(Grievance)
