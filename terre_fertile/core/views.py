from django.shortcuts import render

def home(request):
    context = {
        "titre" : "Bienvenue à Terre Fertile"
    }
    return render(request, 'core/home.html', context)


def about(request):
    members = [
        {"id": 1, "name": "Pierre GEORGES", "role": "DIRECTEUR DE TERRES FERTILES"},
        {"id": 2, "name": "Antoine GODDE", "role": "TECHNICIEN AGRONOME"},
        {"id": 3, "name": "Eloïse COURBIN", "role": "ALTERNANTE INGÉNIEURE AGRONOME (ISARA)"},
    ]
    return render(request, 'core/about.html', {"members": members})

def team_members(request):
    return {
        "members": [
            {"name": "Pierre GEORGES", "role": "DIRECTEUR DE TERRES FERTILES"},
            {"name": "Antoine GODDE", "role": "TECHNICIEN AGRONOME"},
            {"name": "Eloïse COURBIN", "role": "ALTERNANTE INGÉNIEURE AGRONOME (ISARA)"},
        ]
    }

def team(request):
 
    return render(request, 'core/team.html')

def teamDetails(request, member_id):
    members = [
        {"id": 1, "name": "Pierre GEORGES", "role": "DIRECTEUR DE TERRES FERTILES"},
        {"id": 2, "name": "Antoine GODDE", "role": "TECHNICIEN AGRONOME"},
        {"id": 3, "name": "Eloïse COURBIN", "role": "ALTERNANTE INGÉNIEURE AGRONOME (ISARA)"},
    ]
    member = next((m for m in members if m["id"] == member_id), None)
    if member is None:
        # Gérer le cas où le membre n'est pas trouvé
        pass
    return render(request, 'core/team-details.html', {"member": member})