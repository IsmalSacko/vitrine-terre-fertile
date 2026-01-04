import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterModule } from "@angular/router";

@Component({
    selector: 'app-team',
    standalone: true,
    imports: [CommonModule, RouterLink, RouterModule],
    templateUrl: './team.component.html',
    styleUrls: ['./team.component.css']
})
export class TeamComponent {
    members = [
        { name: 'Pierre GEORGES', role: 'DIRECTEUR DE TERRES FERTILES' },
        { name: 'Antoine GODDE', role: 'TECHNICIEN AGRONOME' },
        { name: 'Eloïse COURBIN', role: 'ALTERNANTE INGÉNIEURE AGRONOME (ISARA)' }
    ];
}
