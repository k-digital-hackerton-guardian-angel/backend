from django.contrib import admin
from .models import Crosswalk, CrosswalkManagement

@admin.register(CrosswalkManagement)
class CrosswalkManagementAdmin(admin.ModelAdmin):
    list_display = ('alias', 'extension_time', 'application_time', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('alias',)

@admin.register(Crosswalk)
class CrosswalkAdmin(admin.ModelAdmin):
    list_display = ('crslkManageNo', 'ctprvnNm', 'signguNm', 'roadNm', 'created_at')
    list_filter = ('ctprvnNm', 'signguNm', 'tfclghtYn', 'bcyclCrslkCmbnatYn')
    search_fields = ('crslkManageNo', 'roadNm', 'rdnmadr', 'lnmadr')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('management', 'crslkManageNo', 'crslkKnd')
        }),
        ('Location', {
            'fields': ('ctprvnNm', 'signguNm', 'roadNm', 'rdnmadr', 'lnmadr', 'latitude', 'longitude')
        }),
        ('Features', {
            'fields': ('bcyclCrslkCmbnatYn', 'highlandYn', 'cartrkCo', 'tfclghtYn', 'tfcilndYn')
        }),
        ('Signals', {
            'fields': ('fnctngSgngnrYn', 'sondSgngnrYn', 'greenSgngnrTime', 'redSgngnrTime')
        }),
        ('Time Settings', {
            'fields': ('bt', 'et')
        }),
        ('Additional Features', {
            'fields': ('ftpthLowerYn', 'brllBlckYn', 'cnctrLghtFcltyYn')
        }),
        ('Institution Information', {
            'fields': ('institutionNm', 'instt_name', 'instt_code', 'phoneNumber', 'referenceDate')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
