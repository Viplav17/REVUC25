from django.urls import path
from .views import home, get_food_data

urlpatterns = [
    path('', home, name='home'),
    path('get_food_data/', get_food_data, name='get_food_data'),
]
