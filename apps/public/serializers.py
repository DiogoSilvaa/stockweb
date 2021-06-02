from .models import Prediction
from rest_framework import serializers

class predictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prediction 
        fields = ["sp", "nq", "dw"]
