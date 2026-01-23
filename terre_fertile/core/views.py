from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required

from .models import HomePage, CarouselItem
from .forms import HomePageForm, get_carousel_formset

def home(request):
    # Récupérer le contenu éditable depuis la base
    homepage = HomePage.objects.first()
    carousel_items = CarouselItem.objects.filter(actif=True).order_by('ordre')

    context = {
        "titre": homepage.titre_principal if homepage else "",
        "description": homepage.description if homepage else "",
        "homepage": homepage,
        "carousel_items": carousel_items,
    }
    return render(request, 'core/home.html', context)


@staff_member_required
def home_edit(request):
    homepage = HomePage.objects.first()
    if not homepage:
        homepage = HomePage.objects.create()

    if request.method == 'POST':
        form = HomePageForm(request.POST, request.FILES, instance=homepage)
        formset = get_carousel_formset(data=request.POST, files=request.FILES, instance=homepage)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect(reverse('home'))
    else:
        form = HomePageForm(instance=homepage)
        formset = get_carousel_formset(instance=homepage)

    return render(request, 'core/home_edit.html', {'form': form, 'formset': formset, 'homepage': homepage})


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

def missions(request):
    return render(request, 'core/missions.html')

def contact(request):
    return render(request, 'core/contact.html')