# Employee Search Application
This project contains all the code necessary to reproduce Employee Search Application using Python3 Flask framework as REST API back-end service, Elasticsearch 7 and Angular 8 as client-side. 

This project was developed to help HR department find relevant employees matched by names, skills, projects, certificates, languages. The provided mock-up json data are found in '/back-end/mock-data' directory and replicates real-world human resource data composed of employee profiles, work experience, education, training records etc.

![employee_search2](https://user-images.githubusercontent.com/11573356/64728424-33977100-d4db-11e9-9483-dc62c762342e.gif)


Basic project installation steps:
```
Clone repository

BACK-END:
1. navigate to back-end project
   cd back-end

2. create virtual environment
   virtualenv -p python3 env
   source env/bin/activate

3. install all required libraries
   pip install -r requirements.txt

4. replace Elasticsearch credentials with your credentials
   .env 
   
# ELASTICSEARCH CREDENTIALS LOCALHOST
ELASTICSEARCH_USERNAME_LOCALHOST='REPLACE_THIS_WITH_YOUR_ELASTICSEARCH_USERNAME'
ELASTICSEARCH_PASSWORD_LOCALHOST='REPLACE_THIS_WITH_YOUR_ELASTICSEARCH_PASSWORD'

# ELASTICSEARCH CLOUD CREDENTIALS
ELASTIC_CLOUD_USERNAME='REPLACE_THIS_WITH_YOUR_ELASTIC_CLOUD_USERNAME'
ELASTIC_CLOUD_PASSWORD='REPLACE_THIS_WITH_YOUR_ELASTIC_CLOUD_PASSWORD'

By default Elasticsearch uses:
username = 'elastic'
password = 'changeme'

5. Docker-elk
   git clone git@github.com:deviantony/docker-elk.git 
   cd docker-elk
   sudo docker-compose up

6. create Elasticsearch employees, projects, skills indexes
   python3 indexer.py
   
   employees, projects and skills mappings can be found in
   mappings.py

7. run Flask application
   python3 application.py
   
FRONT-END:
1. cd front-end/employee-search
2. npm install
3. ng serve
```
Angular Routes:
```
locahost:4200 (Home Page)
localhost:4200/search/results/skill (Seach employees by skill)
localhost:4200/search/results/project (Search employees by project)
localhost:4200/employee/<id> (Employee details)
```
Core Functionalities:
```
- Search employees by name, job position, company 
- Search all employees by project 
- Search all employees by skill 
- Show employee details
- Mobile friendly
```
