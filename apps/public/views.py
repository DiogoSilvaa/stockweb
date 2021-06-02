from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prediction
from datetime import datetime
from .serializers import predictionSerializer

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


class day_predictions(APIView):

    def post(self, request):
        data = request.data
        now = datetime.now()
        new_prediction, available = Prediction.objects.get_or_create(date=now, sp=data["sp"], nq=data["nq"], dw=data["dw"])
        if available:
            new_prediction.save()
        predictions = Prediction.objects.all()
        print(predictions)
        return Response(data)

    def get(self, request):
        now = datetime.now()
        todayPrediction = Prediction.objects.get(date=now)
        jsonPred = predictionSerializer(todayPrediction)
        return Response(jsonPred.data)
        
    
    
