import { Routes } from '@angular/router';
import { AboutComponent } from './components/about/about.component';
import { TeamComponent } from './components/team/team.component';

export const routes: Routes = [
    { path: '', component: AboutComponent },
    { path: 'a-propos', component: AboutComponent },
    { path: 'equipe/:id', component: TeamComponent }
];
