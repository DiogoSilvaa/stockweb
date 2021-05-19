from django.urls import path
from .views import index, stock_data

app_name = "public"

urlpatterns = [
    path('api/data', stock_data.as_view()),
    path('', index, name="index")
]