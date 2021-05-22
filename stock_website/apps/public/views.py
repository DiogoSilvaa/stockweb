from django.http import HttpResponse, HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

class stock_data(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
                "sales": 100,
                "customers": 10000,
                }
        return Response(data)
