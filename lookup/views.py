from django.shortcuts import render

def home(request):
    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&
    # API_KEY=66ED8617-4D66-4168-BAB7-371422904ACB
    import json
    import requests

    try:
        response = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=66ED8617-4D66-4168-BAB7-371422904ACB")
        json_data = response.json()
    except Exception as ex:
        error = f"{ex}"
        json_data =  None
        return render(request, 'home.html', {"error": error})
    else:
        return render(request, 'home.html', {"json_data": json_data})

def about(request):
    return render(request, 'about.html', {})