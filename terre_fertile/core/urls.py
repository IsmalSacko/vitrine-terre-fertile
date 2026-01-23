from django.urls import path
from .views import (home, home_edit, about, team, teamDetails, missions, contact)

urlpatterns = [
    path('', home, name='home'),
    path('home/edit/', home_edit, name='home_edit'),
    path('a-propos', about, name='about'),
    path('missions', missions, name='missions'),
    path('contact', contact, name='contact'),
    path('equipe', team, name='team'),
    path('equipe/<int:member_id>', teamDetails, name='team_details'),

]