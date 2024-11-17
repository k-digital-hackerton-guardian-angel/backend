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
    list_filter = (
        'ctprvnNm', 
        'signguNm', 
        'tfclghtYn', 
        'bcyclCrslkCmbnatYn',
        'highlandYn',
        'sondSgngnrYn'
    )
    search_fields = (
        'crslkManageNo', 
        'roadNm', 
        'rdnmadr', 
        'lnmadr',
        'institutionNm',
        'instt_name'
    )
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('기본 정보', {
            'fields': ('management', 'crslkManageNo', 'crslkKnd')
        }),
        ('위치 정보', {
            'fields': ('ctprvnNm', 'signguNm', 'roadNm', 'rdnmadr', 'lnmadr', 'latitude', 'longitude')
        }),
        ('횡단보도 특성', {
            'fields': ('bcyclCrslkCmbnatYn', 'highlandYn', 'cartrkCo', 'tfclghtYn', 'tfcilndYn')
        }),
        ('신호 시스템', {
            'fields': ('fnctngSgngnrYn', 'sondSgngnrYn', 'greenSgngnrTime', 'redSgngnrTime')
        }),
        ('시간 설정', {
            'fields': ('bt', 'et')
        }),
        ('추가 기능', {
            'fields': ('ftpthLowerYn', 'brllBlckYn', 'cnctrLghtFcltyYn')
        }),
        ('기관 정보', {
            'fields': ('institutionNm', 'instt_name', 'instt_code', 'phoneNumber', 'referenceDate')
        }),
        ('메타데이터', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )