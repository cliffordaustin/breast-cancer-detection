from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import MakePredictionSerializer, PredictionsSerializer
from ..models import Predictions

from ..utils import predict_breast_cancer
import os


class MakePredictionView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MakePredictionSerializer(data=request.data)

        if serializer.is_valid():
            image = serializer.validated_data["image"]
            image = image.read()
            model_path = os.path.join(os.getcwd(), "model.h5")
            prediction = predict_breast_cancer(image, model_path)

            return Response({"prediction": prediction}, status=200)
        else:
            return Response(serializer.errors, status=400)


class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Predictions.objects.all()
    serializer_class = PredictionsSerializer


# class PostPrediction
