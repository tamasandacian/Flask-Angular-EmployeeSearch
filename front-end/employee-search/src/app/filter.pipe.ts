import { Pipe, PipeTransform } from '@angular/core';
import { EmployeeService } from './services/employee.service';

@Pipe({
    name: 'filter'
})

export class FilterPipe implements PipeTransform {
    constructor(private employeeService: EmployeeService) {}
    
    transform(employees: any[], searchText: string): any[] {
        if (!employees) return [];
        if (!searchText) return employees;

        searchText = searchText.toLowerCase();

        return employees.filter(emp => {
            this.employeeService.applyFullTextSearch(searchText).subscribe(data => {
                emp = data;
            })
            
            // Apply Elasticsearch Full-text Search on multiple fields:
            //  e.g. Name, Job Position, Company
            if (emp._source.Employee_Name.toLowerCase().includes(searchText)) {
                return emp._source.Employee_Name.toLowerCase().includes(searchText); 
            }

            if (emp._source.Position.toLowerCase().includes(searchText)) {
                return emp._source.Position.toLowerCase().includes(searchText); 
            }

            if (emp._source.Company.toLowerCase().includes(searchText)) {
                return emp._source.Company.toLowerCase().includes(searchText); 
            }
        });
    }
}