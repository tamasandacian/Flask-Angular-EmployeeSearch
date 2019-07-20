from elasticsearch import Elasticsearch
from elasticsearch import exceptions

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import credentials as cred

import json
import os

# Create elasticsearch instance
es = Elasticsearch(cred.ES_HOST, http_auth=(cred.username, cred.password))

# Check Elasticsearch connection
if not es.ping():
    raise ValueError("Connection failed ...")

application = Flask(__name__)
# Allow CORS Origin to perform requests from Angular project
CORS(application, resources={r"/api/*": {"origins": "*"}})

# GET ALL EMPLOYEES
@application.route('/api/employees', methods=['GET'])
def get_all_employees():
    """ 
    Method to return all employees as json response 
    """
    print("-" * 50)
    results = es.search(index='employees')
    print("######### Employees: #########\n")
    print(json.dumps(results['hits']['hits']))
    print("-" * 50)
    return jsonify(results['hits']['hits'])

# GET EMPLOYEE BY ID
@application.route('/api/employee/<id>', methods=['GET'])
def get_employee_by_id(id):
    """ 
    Method to return employee details as json response object querying on 
    id parameter.
    """
    print("-" * 50)
    print("EmployeeID: " + id + "\n")
    result = es.search(
        index="employees",
        body={
            "query": {
                "match": {
                    "Employee_ID": id
                }
            }
        })

    print("######## Employee details with id=" + id + " #########\n")
    print(json.dumps(result))
    print("-" * 50)
    return jsonify(result['hits']['hits'][0])


# APPLY FULL TEXT SEARCH EMPLOYEE BY NAME
@application.route('/api/employees/search/<term>', methods=['GET'])
def get_employee_by_multiple_fields(term):
    """ 
    Method to return an array of employees as json response querying on
    multiple fields. 
    """
    print("-" * 50)
    print("Term: " + term + "\n")
    result = es.search(
        index="employees",
        body={
            "query": {
                "multi_match": {
                    "query": term,
                    "fields": ["Employee_Name", "Position", "Company"]
                }
            }
        })
    print("######### Employees with term=" + term + " #########\n")
    print(json.dumps(result['hits']['hits']))
    print("-" * 50)
    return jsonify(result['hits']['hits'])


# GET ALL PROJECTS
@application.route('/api/projects', methods=['GET'])
def get_all_projects():
    """ 
    Method to return an array of json project response. 
    """
    print("-" * 50)
    results = es.search(index='projects')
    print("######### Projects: #########\n")
    print(json.dumps(results['hits']['hits']))
    print("-" * 50)
    return jsonify(results['hits']['hits'])


# SEARCH EMPLOYEES BY CURRENT PROJECT NAME
@application.route('/api/employees/search/current/project/<term>', methods=['GET'])
def get_employees_by_current_project(term):
    """ 
    Method to return an array of employees by project as json response. 
    """
    print("-" * 50)
    print("Term: " + term + "\n")
    results = es.search(
        index="projects",
        body={
            "query": {
                "match_phrase": {
                    "Project_Name": term
                }
            },
            "_source": ["Project_Name", "People", "Status"]
        })
    print("######### Employees by " + term + " project #########\n")
    print(json.dumps(results))
    print("-" * 50)
    return jsonify(results['hits']['hits'])


# GET ALL SKILLS
@application.route('/api/skills', methods=['GET'])
def get_all_skills():
    """ 
    Method to return an array of skills as json response. 
    """
    print("-" * 50)
    results = es.search(index='skills')
    print("######## Skills: ########\n")
    print(json.dumps(results['hits']['hits']))
    print("-" * 50)
    return jsonify(results['hits']['hits'])

# SEARCH EMPLOYEES BY SKILLS
@application.route('/api/employees/search/skill/<term>', methods=['GET'])
def get_employees_by_skill(term):
    """ 
    Method to return an array of employees by skill as json response. 
    """
    print("-" * 50)
    print("Term: " + term + "\n")
    results = es.search(
        index="skills",
        body={
            "query": {
                "match_phrase": {
                    "Skill": term
                }
            },
            "_source": ["Skill", "People"]
        })
    print("######### Employees by " +  term + " skill #########\n")
    print(json.dumps(results['hits']['hits']))
    print("-" * 50)
    return jsonify(results['hits']['hits'])


if __name__ == "__main__":
    application.debug = True  # it should be used only in development not production
    application.run()
