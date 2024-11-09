from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from ..models import Predictions


class PredictionsSerializer(ModelSerializer):
    class Meta:
        model = Predictions
        fields = "__all__"


class MakePredictionSerializer(Serializer):
    image = serializers.ImageField()
