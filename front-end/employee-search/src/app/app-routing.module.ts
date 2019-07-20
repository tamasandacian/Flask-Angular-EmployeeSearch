import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { EmployeeDetailsComponent } from './components/employee-details/employee-details.component';
import { SkillsComponent } from './components/skills/skills.component';
import { ProjectsComponent } from './components/projects/projects.component';

const routes: Routes = [
  ////////////////////////////// EMPLOYEE SEARCH ROUTES //////////////////////////////////
  { path: '', component: HomeComponent },
  { path: 'employee/:id', component: EmployeeDetailsComponent },
  { path: 'search/results/skill', component: SkillsComponent },
  { path: 'search/results/project', component: ProjectsComponent },
  ////////////////////////////////////////////////////////////////////////////////////////
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
