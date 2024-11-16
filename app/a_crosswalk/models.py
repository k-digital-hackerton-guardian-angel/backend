from django.db import models


class Crosswalk(models.Model):
    ctprvnNm = models.CharField(max_length=100) # 시도명
    signguNm = models.CharField(max_length=100) # 시군구명
    roadNm = models.CharField(max_length=100) # 도로명
    rdnmadr = models.CharField(max_length=255) # 소재지도로명주소
    lnmadr = models.CharField(max_length=255) # 소재지지번주소
    crslkManageNo = models.CharField(max_length=50) # 횡단보도관리번호
    crslkKnd = models.CharField(max_length=50) # 횡단보도종류
    bcyclCrslkCmbnatYn = models.BooleanField() # 자전거횡단도겸용여부
    highlandYn = models.BooleanField() # 고원식적용여부
    latitude = models.FloatField() # 위도
    longitude = models.FloatField() # 경도
    cartrkCo = models.IntegerField() # 차로수
    bt = models.TimeField() # 횡단보도폭
    et = models.TimeField() # 횡단보도연장
    tfclghtYn = models.BooleanField() # 보행자신호등유무
    fnctngSgngnrYn = models.BooleanField() # 보행자작동신호기유무
    sondSgngnrYn = models.BooleanField() # 음향신호기설치여부
    greenSgngnrTime = models.TimeField() # 녹색신호시간
    redSgngnrTime = models.TimeField() # 적색신호시간
    tfcilndYn = models.BooleanField() # 교통섬유무
    ftpthLowerYn = models.BooleanField() # 보도턱낮춤여부
    brllBlckYn = models.BooleanField() # 점자블록유무
    cnctrLghtFcltyYn = models.BooleanField() # 집중조명시설유무
    institutionNm = models.CharField(max_length=100) # 관리기관명
    phoneNumber = models.CharField(max_length=20) # 관리기관전화번호
    referenceDate = models.DateField() # 데이터기준일자
    instt_code = models.CharField(max_length=50) # 제공기관코드

    def __str__(self):
        return self.lnmadr
