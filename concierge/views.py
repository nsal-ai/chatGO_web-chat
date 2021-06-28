from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
#from chatterbot import ChatBot
#from chatterbot.ext.django_chatterbot import settings
#from concierge.google_API import GoogleMapsClient, GooglePlaces


# Create your views here.     


def concierge(request):
    
    return render(request, 'chat/concierge.html')

# class GetRestaurantData(TemplateView):
#     template_name = 'chat/concierge.html'
#     def search_places_by_coordinate(self, *args, **kwargs):
#         context = {
#             'geolocation' : (),
#         }
#         return context
 
def bot_search(request):
    query = request.GET.get('query')



from django.http import HttpResponse
from django.forms import Form
from django.views.decorators.csrf import csrf_exempt
from concierge.google_api import *


@csrf_exempt
def restaurant_data(request):
    if request.method == "POST":
        location = request.POST["location"]
        
        
        context = {
          'location': location,
          'results': search_restaurant(location)
        }
        return render(request, "chat/rest_location.html", context=context)

    else:
        return render(request, "chat/rest_location.html")






