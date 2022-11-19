# from django.db import models
from django.contrib.gis.db import models as gis_models

from ..base_app.models import BaseModel


class Hemo(BaseModel):
    title = gis_models.CharField(max_length=255, verbose_name="Nome")
    latitude = gis_models.PointField(verbose_name="Latitude")
    longitude = gis_models.PointField(verbose_name="Longitude")
