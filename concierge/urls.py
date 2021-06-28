from django.urls import path
from . import views


urlpatterns = [
    path('concierge/', views.concierge, name='concierge'),
    path('concierge/restaurant_data', views.restaurant_data, name= 'concierge'),
   
]


