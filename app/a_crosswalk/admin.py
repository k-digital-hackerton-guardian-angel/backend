from django.contrib import admin
from .models import Crosswalk, CrosswalkManagement

class CrosswalkManagementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CrosswalkManagement._meta.fields]

class CrosswalkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Crosswalk._meta.fields]

admin.site.register(Crosswalk, CrosswalkAdmin)
admin.site.register(CrosswalkManagement, CrosswalkManagementAdmin)

