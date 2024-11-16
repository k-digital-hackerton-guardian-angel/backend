from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from a_crosswalk.api import router as crosswalk_router

api = NinjaAPI()

api.add_router("/crosswalks/", crosswalk_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
