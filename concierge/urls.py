from django.urls import path

from . import views

urlpatterns = [
    
    path('concierge/', views.concierge, name='concierge'),
    
    
]


