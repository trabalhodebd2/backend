from rest_framework import serializers

from ..models import Hemo


class HemoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Hemo
        fields = "__all__"
