from elasticsearch import Elasticsearch
from elasticsearch import exceptions
from elasticsearch import connection

import mappings as mp
import credentials as cred
import json
import os
import sys

# Create elasticsearch instance
es = Elasticsearch(cred.ES_HOST, http_auth=(cred.username, cred.password))

class Indexer():
    """
    Class for creating mappings (employees, projects, skills)
    and ingest json data to its corresponding index.
    """

    def create_mapping(self, index, body):
        """
        Method to create index for employees, project and skill.
        """
        try:
            es.indices.put_mapping(
                index=index, 
                doc_type="generated",
                body=body)
            print("-" * 50)
            print('Index created successfully!')
            
            return True
        except exceptions.RequestError:
            print("-" * 50)
            print('Index already exists')
            return False
        except Exception as e:
            print('-' * 50)
            print('An unknown error occured while connecting to Elasticsearch ...')
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

    def index_data(self, input_dir_file):
        """
        Method to ingest data to elasticsearch indexes.
        """
        for filepath in os.listdir(input_dir_file):
            if filepath.startswith('employees'):
                path = "./mock_data/employees.json"
                with open(path) as f:

                    employee = {}
                    json_data = json.loads(f.read())

                    for line in json_data:
                        try:
                            # Check if following properties exist in the json file
                            if ("Employee_ID" or "Employee_Name" or "Company" or "MD" or "Position" or "Join_Date" or "Telephone" or "Email" or "Image_URL" or "Project_Role") in line:
                                employee_id = line["Employee_ID"]
                                employee_name = line["Employee_Name"]
                                company = line["Company"]
                                md = line["MD"]
                                position = line["Position"]
                                join_date = line["Join_Date"]
                                telephone = line["Telephone"]
                                email = line["Email"]
                                image_url = line["Image_URL"]
                                project_role = line["Project_Role"]

                                current_projects = []
                                current_project = {}

                                # Check if "Current_Projects" property exists and contains at least 1 element
                                if "Current_Projects" in line and len(line["Current_Projects"]) > 0:
                                    for current_project in line["Current_Projects"]:
                                        current_project_id = current_project["Project_ID"]
                                        current_project_name = current_project["Project_Name"]
                                        current_project_from = current_project["From"]
                                        current_project_to = current_project["To"]
                                        current_project = {
                                            "Project_ID": current_project_id,
                                            "Project_Name": current_project_name,
                                            "From": current_project_from,
                                            "To": current_project_to
                                        }
                                        current_projects.append(current_project)

                                past_projects = []
                                past_project = {}

                                # Check if "Past_Projects" property exists and contains at least 1 element
                                if "Past_Projects" in line:
                                    for past_project in line["Past_Projects"]:
                                        past_project_id = past_project["Project_ID"]
                                        past_project_name = past_project["Project_Name"]
                                        past_project_from = past_project["From"]
                                        past_project_to = past_project["To"]
                                        past_project = {
                                            "Project_ID": past_project_id,
                                            "Project_Name": past_project_name,
                                            "From": past_project_from,
                                            "To": past_project_to
                                        }
                                        past_projects.append(past_project)

                                next_projects = []
                                next_project = {}

                                # Check if "Next_Projects" property exists and contains at least 1 element
                                if "Next_Projects" in line and len(line["Next_Projects"]) > 0:
                                    for next_project in line["Next_Projects"]:
                                        next_project_id = next_project["Project_ID"]
                                        next_project_name = next_project["Project_Name"]
                                        next_project_from = next_project["From"]
                                        next_project_to = next_project["To"]
                                        next_project = {
                                            "Project_ID": next_project_id,
                                            "Project_Name": next_project_name,
                                            "From": next_project_from,
                                            "To": next_project_to
                                        }
                                        next_projects.append(next_project)

                                educations = []
                                education = {}

                                # Check if "Education" property exists and contains at least 1 element
                                if "Education" in line and len(line["Education"]) > 0:
                                    for ed in line["Education"]:
                                        degree_type = ed["Degree_Type"]
                                        from_date = ed["From_Date"]
                                        to_date = ed["To_Date"]
                                        qualification = ed["Qualification"]
                                        institute = ed["Institute"]
                                        faculty = ed["Faculty"]
                                        subject = ed["Subject"]
                                        gpa = ed["GPA"]
                                        education = {
                                            "Degree_Type": degree_type,
                                            "From_Date": from_date,
                                            "To_Date": to_date,
                                            "Qualification": qualification,
                                            "Institute": institute,
                                            "Faculty": faculty,
                                            "Subject": subject,
                                            "GPA": gpa
                                        }
                                        educations.append(education)

                                training_courses = []
                                training_course = {}

                                # Check if "Training_Courses" property exists and contains at least 1 element
                                if "Training_Courses" in line and len(line["Training_Courses"]) > 0:
                                    for tc in line["Training_Courses"]:
                                        training_course = tc["Training_Course"]
                                        first_training_date = tc["First_Training_Date"]
                                        year = tc["Year"]
                                        course_status = tc["Course_Status"]
                                        training_course = {
                                            "Training_Course": training_course,
                                            "First_Training_Date": first_training_date,
                                            "Year": year,
                                            "Course_Status": course_status
                                        }
                                        training_courses.append(
                                            training_course)

                                skills = []
                                # Check if "Skills" exists property exists and contains at least 1 element
                                if "Skills" in line and len(line["Skills"]) > 0:
                                    for skill in line["Skills"]:
                                        skills.append(skill)

                                languages = []
                                # Check if "Languages" exists property exists and contains at least 1 element
                                if "Languages" in line and len(line["Languages"]) > 0:
                                    for language in line["Languages"]:
                                        languages.append(language)

                                employee = {
                                        "Employee_ID": employee_id,
                                        "Employee_Name": employee_name,
                                        "Company": company,
                                        "MD": md,
                                        "Position": position,
                                        "Join_Date": join_date,
                                        "Telephone": telephone,
                                        "Email": email,
                                        "Image_URL": image_url,
                                        "Project_Role": project_role,
                                        "Past_Projects": past_projects,
                                        "Current_Projects": current_projects,
                                        "Next_Projects": next_projects,
                                        "Education": educations,
                                        "Training_Courses": training_courses,
                                        "Skills": skills,
                                        "Languages": languages
                                }

                                print("-" * 50)
                                print("Employee:")
                                print(employee)

                                es.index(index='employees', doc_type='generated', id=employee_id, body=employee)

                        except Exception as e:
                            print('Some error occured while indexing employee data ...')
                            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                            break

            elif filepath.startswith('project'):
                path = "./mock_data/project.json"
                with open(path) as f:
                    project = {}
                    json_data = json.loads(f.read())
                    for line in json_data:
                        try:
                            if ("Project_Name" or "Status") in line:
                                project_name = line["Project_Name"]
                                status = line["Status"]

                            people = []
                            employee = {}

                            if "People" in line and len(line["People"]) > 0:
                                for emp in line["People"]:
                                    employee_id = emp["Employee_ID"]
                                    employee_name = emp["Employee_Name"]
                                    employee = {
                                        "Employee_ID": employee_id,
                                        "Employee_Name": employee_name
                                    }
                                    people.append(employee) 

                            project = {
                                "Project_Name": project_name,
                                "Status": status,
                                "People": people
                            }

                            print("-" * 50)
                            print("Project:")
                            print(project)

                            es.index(index='projects', doc_type='generated', body=project)

                        except Exception as e:
                            print('Error occured while indexing project data ...')
                            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                            break
            
            else:
                path = "./mock_data/skill.json"
                with open(path) as f:
                    skill = {}
                    json_data = json.loads(f.read())
                    for line in json_data:
                        try:
                            if "Skill" in line:
                                skill_name = line["Skill"]

                            people = []
                            employee = {}
                            if "People" in line and len(line["People"]) > 0:
                                for emp in line["People"]:
                                    employee_id = emp["Employee_ID"]
                                    employee_name = emp["Employee_Name"]
                                    employee = {
                                        "Employee_ID": employee_id,
                                        "Employee_Name": employee_name
                                    }
                                    people.append(employee)

                            skill = {
                                "Skill": skill_name,
                                "People": people
                            }

                            print("-" * 50)
                            print("Skill:")
                            print(skill)
                           
                            es.index(index='skills', doc_type='generated', body=skill)

                        except Exception as e:
                            print('Error occured while indexing skill data ...')
                            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                            break
            


if __name__ == "__main__":

    # Create elasticsearch mappings
    indexer = Indexer()
    indexer.create_mapping("employees", mp.employees_mapping)
    indexer.create_mapping("projects", mp.projects_mapping)
    indexer.create_mapping("skills", mp.skills_mapping)
    
    # Index data to elasticsearch from specified directory
    input_dir_file = "./mock_data"
    indexer.index_data(input_dir_file)
