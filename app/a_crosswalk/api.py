# app/a_crosswalk/api.py

from ninja import Router, Query
from typing import List
from .models import Crosswalk
from django.shortcuts import get_object_or_404
from .schemas import CrosswalkSchemaOut, CrosswalkSchemaIn, BoundingBoxSchema

router = Router()


@router.get("/area", response=List[CrosswalkSchemaOut])
def get_crosswalks_in_area(request, bounds: BoundingBoxSchema = Query(...)):
    min_latitude = min(bounds.min_lat, bounds.max_lat)
    max_latitude = max(bounds.min_lat, bounds.max_lat)
    min_longitude = min(bounds.min_lng, bounds.max_lng)
    max_longitude = max(bounds.min_lng, bounds.max_lng)

    crosswalks = Crosswalk.objects.filter(
        latitude__gte=min_latitude,
        latitude__lte=max_latitude,
        longitude__gte=min_longitude,
        longitude__lte=max_longitude,
    )[:30]
    return crosswalks


@router.get("/time", response=List[CrosswalkSchemaOut])
def get_crosswalks_in_time(request):
    crosswalks = Crosswalk.objects.filter(increaseInGreenTime30__isnull=False)
    return crosswalks
