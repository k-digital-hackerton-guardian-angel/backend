from ninja import Schema
from datetime import date, time
from typing import Optional

class CrosswalkSchemaOut(Schema):
    id: int
    ctprvnNm: str
    signguNm: str
    roadNm: str
    rdnmadr: str
    lnmadr: str
    crslkManageNo: str
    crslkKnd: str
    bcyclCrslkCmbnatYn: bool
    highlandYn: bool
    latitude: float
    longitude: float
    cartrkCo: int
    bt: str
    et: str
    tfclghtYn: bool
    fnctngSgngnrYn: bool
    sondSgngnrYn: bool
    greenSgngnrTime: str
    redSgngnrTime: str
    tfcilndYn: bool
    ftpthLowerYn: bool
    brllBlckYn: bool
    cnctrLghtFcltyYn: bool
    institutionNm: str
    phoneNumber: str
    referenceDate: str
    instt_code: str
    management: int
    increaseInGreenTime30: Optional[int] = None
    increaseInGreenTime50: Optional[int] = None
    applyTimeFrom: Optional[str] = None
    applyTimeTo: Optional[str] = None
    

    @staticmethod
    def resolve_bt(obj) -> str:
        return obj.bt.strftime('%H:%M:%S') if obj.bt else '00:00:00'
    
    @staticmethod
    def resolve_et(obj) -> str:
        return obj.et.strftime('%H:%M:%S') if obj.et else '00:00:00'
    
    @staticmethod
    def resolve_greenSgngnrTime(obj) -> str:
        return obj.greenSgngnrTime.strftime('%H:%M:%S') if obj.greenSgngnrTime else '00:00:00'
    
    @staticmethod
    def resolve_redSgngnrTime(obj) -> str:
        return obj.redSgngnrTime.strftime('%H:%M:%S') if obj.redSgngnrTime else '00:00:00'
    
    @staticmethod
    def resolve_referenceDate(obj) -> str:
        return obj.referenceDate.strftime('%Y-%m-%d') if obj.referenceDate else '2024-01-01'
    
    @staticmethod
    def resolve_management(obj) -> int:
        return obj.management.id if obj.management else None
    
    @staticmethod
    def resolve_applyTimeFrom(obj) -> str:
        return obj.applyTimeFrom.strftime('%H:%M:%S') if obj.applyTimeFrom else '00:00:00'
    
    @staticmethod
    def resolve_applyTimeTo(obj) -> str:
        return obj.applyTimeTo.strftime('%H:%M:%S') if obj.applyTimeTo else '00:00:00'

class CrosswalkSchemaIn(Schema):
    ctprvnNm: str
    signguNm: str
    roadNm: str
    rdnmadr: str
    lnmadr: str
    crslkManageNo: str
    crslkKnd: str
    bcyclCrslkCmbnatYn: bool
    highlandYn: bool
    latitude: float
    longitude: float
    cartrkCo: int
    bt: str
    et: str
    tfclghtYn: bool
    fnctngSgngnrYn: bool
    sondSgngnrYn: bool
    greenSgngnrTime: str
    redSgngnrTime: str
    tfcilndYn: bool
    ftpthLowerYn: bool
    brllBlckYn: bool
    cnctrLghtFcltyYn: bool
    institutionNm: str
    phoneNumber: str
    referenceDate: str
    instt_code: str
    management: int
    increaseInGreenTime30: Optional[int] = None
    increaseInGreenTime50: Optional[int] = None
    applyTimeFrom: Optional[str] = None
    applyTimeTo: Optional[str] = None

class BoundingBoxSchema(Schema):
    min_lat: float
    min_lng: float
    max_lat: float
    max_lng: float
