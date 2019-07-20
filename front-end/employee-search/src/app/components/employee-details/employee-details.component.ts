import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { EmployeeService } from 'src/app/services/employee.service';

@Component({
  selector: 'app-employee-details',
  templateUrl: './employee-details.component.html',
  styleUrls: ['./employee-details.component.css']
})
export class EmployeeDetailsComponent implements OnInit {

  employee: Object;
  employeeID: number;

  constructor(private route: ActivatedRoute, private employeeService: EmployeeService) {
 
      this.route.params.subscribe((params: Params) => {
        this.employeeID = params['id'];
      })
      

   }

  ngOnInit() {
    this.getEmployeeByID();
  }

  getEmployeeByID() {
    this.employeeService.getEmployeeByID(this.employeeID).subscribe(data => {
      this.employee = data;
      console.log(this.employee)
    })
  }

}
