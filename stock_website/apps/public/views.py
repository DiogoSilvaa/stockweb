from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')
