# from django.db import models
from django.contrib.gis.db import models as gis_models

from ..base_app.models import BaseModel


class Hemo(BaseModel):
    title = gis_models.CharField(max_length=255, verbose_name="Nome")
    geometry = gis_models.PointField(verbose_name="Latitude")
    city = gis_models.CharField(
        max_length=255, verbose_name="Cidade", blank=True, null=True
    )
    uf = gis_models.CharField(
        max_length=2, verbose_name="Estado", blank=True, null=True
    )
