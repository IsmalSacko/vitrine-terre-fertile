from django.urls import path
from .views import (home, about, team, teamDetails)

urlpatterns = [
    path('', home, name='home'),
    path('a-propos', about, name='about'),
    
    path('equipe/<int:member_id>', teamDetails, name='team_details'),
]