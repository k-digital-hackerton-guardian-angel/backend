# app/a_crosswalk/api.py

from ninja import Router
from typing import List
from .models import Crosswalk
from django.shortcuts import get_object_or_404
from .schemas import CrosswalkSchemaOut, CrosswalkSchemaIn

router = Router()

@router.get("/crosswalks", response=List[CrosswalkSchemaOut])
def list_crosswalks(request):
    qs = Crosswalk.objects.all()
    return qs

@router.get("/crosswalks/{crosswalk_id}", response=CrosswalkSchemaOut)
def get_crosswalk(request, crosswalk_id: int):
    crosswalk = get_object_or_404(Crosswalk, id=crosswalk_id)
    return crosswalk

@router.post("/crosswalks", response=CrosswalkSchemaOut)
def create_crosswalk(request, data: CrosswalkSchemaIn):
    crosswalk = Crosswalk.objects.create(**data.dict())
    return crosswalk

@router.put("/crosswalks/{crosswalk_id}", response=CrosswalkSchemaOut)
def update_crosswalk(request, crosswalk_id: int, data: CrosswalkSchemaIn):
    crosswalk = get_object_or_404(Crosswalk, id=crosswalk_id)
    for attr, value in data.dict().items():
        setattr(crosswalk, attr, value)
    crosswalk.save()
    return crosswalk

@router.delete("/crosswalks/{crosswalk_id}", response={200: str})
def delete_crosswalk(request, crosswalk_id: int):
    crosswalk = get_object_or_404(Crosswalk, id=crosswalk_id)
    crosswalk.delete()
    return 200, "Crosswalk deleted successfully."