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
        """ Try catch error """
        data = request.data
        now = datetime.now()
        new_prediction, is_new = Prediction.objects.get_or_create(date=now, sp=data["sp"], nq=data["nq"], dw=data["dw"])
        if is_new:
            new_prediction.save()
        #predictions = Prediction.objects.all()
        print(new_prediction.sp, new_prediction.nq, new_prediction.dw)
        return Response()

    def get(self, request):
        todayPrediction = Prediction.objects.latest('date')
        jsonPred = predictionSerializer(todayPrediction)
        return Response(jsonPred.data)
        
    
    
