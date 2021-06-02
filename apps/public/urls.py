from django.urls import path
from .views import index, day_predictions

app_name = "public"

urlpatterns = [
    path('', index, name="index"),
    path('api/data/', day_predictions.as_view()),
]