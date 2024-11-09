from django import urls
from .views import MakePredictionView, PatientListCreateView


urlpatterns = [
    urls.path("make-prediction/", MakePredictionView.as_view(), name="make-prediction"),
    urls.path("patients/", PatientListCreateView.as_view(), name="patients"),
]
