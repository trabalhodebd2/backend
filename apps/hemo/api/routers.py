from rest_framework.routers import DefaultRouter

from .viewsets import *

hemo_router = DefaultRouter()
hemo_router.register("hemos", HemoViewset, basename="api-hemos")
