import { Component, OnInit } from '@angular/core';
import { EmployeeService } from 'src/app/services/employee.service';


@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css'],
})
export class ProjectsComponent implements OnInit {

  projects: any [] = [];
  objectKeys = Object.keys;

  constructor(private employeeService: EmployeeService) { }

  ngOnInit() {
    this.get_all_projects_by_default();
  }

  get_all_projects_by_default() {
    
    this.employeeService.getAllProjects().subscribe(data => {
      this.projects = data
    });
  
  }

  search(term: string) {
    // Check if input term
    if (!term) return this.get_all_projects_by_default();

    // Perform lowecase input string
    term = term.toLowerCase();
    if (term) {
      this.employeeService.searchByCurrentProject(term).subscribe(data => {
        this.projects = data;
      });
    }
  }

}
