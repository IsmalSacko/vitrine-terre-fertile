import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TeamComponent } from '../team/team.component';

@Component({
    selector: 'app-about',
    standalone: true,
    imports: [CommonModule, TeamComponent],
    templateUrl: './about.component.html',
    styleUrls: ['./about.component.css']
})
export class AboutComponent { }
