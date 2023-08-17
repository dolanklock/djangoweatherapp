from django.shortcuts import render
from . import constants

# TODO: handle exception raised when search is empty
def main_render(request, zipcode: str):
    import json
    import requests
    try:
        response = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=66ED8617-4D66-4168-BAB7-371422904ACB")
        json_data = response.json()
        if len(json_data) == 0:
            return render(request, 'home.html', {"error": "Enter a valid zipcode"})
    except Exception as ex:
        error = f"{ex}"
        json_data =  None
        return render(request, 'home.html', {"error": error})
    else:
        if json_data[0]["Category"]["Name"] == "Good":
            category_description = constants.AIR_QUALITY_DESCRIPTIONS["good"]
            category_color = "good"
        if json_data[0]["Category"]["Name"] == "Moderate":
            category_description = constants.AIR_QUALITY_DESCRIPTIONS["moderate"]
            category_color = "moderate"
        if json_data[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            category_description = constants.AIR_QUALITY_DESCRIPTIONS["usg"]
            category_color = "usg"
        return render(request, 'home.html', {"json_data": json_data,
                                            "category_description": category_description,
                                            "category_color": category_color,
                                            })

def home(request):
    if request.method == "POST":  # checking if request is a POST request. (base html file in form has "method=POST")
        zipcode = request.POST["zipcode"]  # getting the value from 'name' attirbute from base html forms element
        return main_render(request=request, zipcode=zipcode)  # has to return the HTTPS response
    
    else:
        return main_render(request=request, zipcode="89129")  # has to return the HTTPS response


def about(request):
    return render(request, 'about.html', {})




# def home(request):
#     import json
#     import requests

#     if request.method == "POST":  # checking if request is a POST request
#         zipcode = request.POST["zipcode"]  # getting the value from 'name' attirbute from base html
#         try:
#             response = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=66ED8617-4D66-4168-BAB7-371422904ACB")
#             json_data = response.json()
#         return render(request, 'home.html', {'zipcode': zipcode})
    
#     else:
#         try:
#             response = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=66ED8617-4D66-4168-BAB7-371422904ACB")
#             json_data = response.json()
#         except Exception as ex:
#             error = f"{ex}"
#             json_data =  None
#             return render(request, 'home.html', {"error": error})
#         else:
#             if json_data[0]["Category"]["Name"] == "Good":
#                 category_description = constants.AIR_QUALITY_DESCRIPTIONS["good"]
#                 category_color = "good"
#             if json_data[0]["Category"]["Name"] == "Moderate":
#                 category_description = constants.AIR_QUALITY_DESCRIPTIONS["moderate"]
#                 category_color = "moderate"
#             if json_data[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
#                 category_description = constants.AIR_QUALITY_DESCRIPTIONS["usg"]
#                 category_color = "usg"
#             return render(request, 'home.html', {"json_data": json_data,
#                                                 "category_description": category_description,
#                                                 "category_color": category_color,
#                                                 })