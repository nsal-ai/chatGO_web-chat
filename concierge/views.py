from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
#from chatterbot import ChatBot
#from chatterbot.ext.django_chatterbot import settings







# Create your views here.     

def concierge(request):
   
    return render(request, 'chat/concierge.html')


# Geocoding API
# Places API



# class ChatterBotApiView(View):
#     """
#     Provide an API endpoint to interact with ChatterBot.
#     """
    

#     chatterbot = ChatBot(**settings.CHATTERBOT)

    
#     def post(self, request, *args, **kwargs):
#         """
#         Return a response to the statement in the posted data.
#         * The JSON data should contain a 'text' attribute.
#         """
#         input_data = json.loads(request.body.decode('utf-8'))

#         if 'text' not in input_data:
#             return JsonResponse({
#                 'text': [
#                     'The attribute "text" is required.'
#                 ]
#             }, status=400)

#         response = self.chatterbot.get_response(input_data)

#         response_data = response.serialize()

#         return JsonResponse(response_data, status=200)

#     def get(self, request, *args, **kwargs):
#         """
#         Return data corresponding to the current conversation.
#         """
#         return JsonResponse({
#             'name': self.chatterbot.name
#         })

