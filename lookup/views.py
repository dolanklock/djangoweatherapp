# this is my views.py file
from django.shortcuts import render

# Create your views here.

def home(request):
    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&
    # API_KEY=66ED8617-4D66-4168-BAB7-371422904ACB
    import json
    import requests
    response = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=66ED8617-4D66-4168-BAB7-371422904ACB")
    response.raise_for_status()
    json_data = response.json()
    return render(request, 'home.html', {"json_data": json_data})

def about(request):
    return render(request, 'about.html', {})