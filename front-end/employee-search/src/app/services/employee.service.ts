import { Injectable } from '@angular/core';
import { AppConfig } from '../app-config';
import { HttpClient } from '@angular/common/http';
import { Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {
  constructor(private http: HttpClient, private appConfig: AppConfig) { }

  // GET ALL EMPLOYEES
  getAllEmployees(): Observable<any> {
    return this.http.get(this.appConfig.apiUrl + '/api/employees');
  }

  // GET EMPLOYEES BY ID
  getEmployeeByID(id: any): Observable<any> {
    return this.http.get(this.appConfig.apiUrl + '/api/employee/' + id);
  }

  // APPLY FULL TEXT SEARCH EMPLOYEE BY NAME
  applyFullTextSearch(term: string): any {
    return this.http.get(this.appConfig.apiUrl + "/api/employees/search/" + term)
  }

  // GET ALL PROJECTS
  getAllProjects(): Observable<any> {
    return this.http.get(this.appConfig.apiUrl + "/api/projects")
  }

  // SEARCH EMPLOYEES BY CURRENT PROJECT NAME
  searchByCurrentProject(term: string): any {
    return this.http.get(this.appConfig.apiUrl + "/api/employees/search/current/project/" + term)
  }
  
  // GET ALL SKILLS
  getAllSkills(): Observable<any> {
      return this.http.get(this.appConfig.apiUrl + "/api/skills")
  }
  // SEARCH EMPLOYEES BY SKILL NAME
  searchBySkillName(term: string): any {
    return this.http.get(this.appConfig.apiUrl + "/api/employees/search/skill/" + term)
  }
}
