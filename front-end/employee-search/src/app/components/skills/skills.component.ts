import { Component, OnInit } from '@angular/core';
import { EmployeeService } from 'src/app/services/employee.service';


@Component({
  selector: 'app-skills',
  templateUrl: './skills.component.html',
  styleUrls: ['./skills.component.css']
})
export class SkillsComponent implements OnInit {

  skills_data: any [] = [];

  constructor(private employeeService: EmployeeService) { }

  ngOnInit() {
    this.get_all_skills_by_default();
  }

  get_all_skills_by_default() {
   this.employeeService.getAllSkills().subscribe(data => {
    this.skills_data = data
  });
  }

  search(term: string) {
    // Check if input term
    if (!term) return this.get_all_skills_by_default();

    // Perform lowecase input string
    term = term.toLowerCase();
    if (term) {
      this.employeeService.searchBySkillName(term).subscribe(data => {
        this.skills_data = data;
      });
    }
  }
}
