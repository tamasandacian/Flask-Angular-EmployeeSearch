import { Component, OnInit } from '@angular/core';
import { EmployeeService } from 'src/app/services/employee.service';

@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  employees: any[] = [];
  searchText: string = '';

  constructor(private employeeService: EmployeeService) {
    this.searchText = '';
  }

  ngOnInit() {
    this.getEmployees()
  }

  getEmployees() {
    this.employeeService.getAllEmployees().subscribe(data => {
      this.employees = data;
    })
  }

  search() {
    let term = this.searchText;
    this.employeeService.applyFullTextSearch(term).subscribe(data => {
      this.employees = data;
    })

  }

}
