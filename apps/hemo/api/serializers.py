from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from ..models import Hemo


class HemoSerializer(GeoFeatureModelSerializer):
    class Meta:

        model = Hemo
        fields = "__all__"
        geo_field = "geometry"
