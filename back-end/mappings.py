
employees_mapping = '''
{
    "mappings": {
        "properties": {
            "Company": {
                "type": "text"
            },
            "Current_Projects": {
                "type": "nested",
                "include_in_parent": true,
                "properties": {
                    "From": {
                        "type": "text"
                    },
                    "Project_ID": {
                        "type": "text"
                    },
                    "Project_Name": {
                        "type": "text"
                    },
                    "To": {
                        "type": "text"
                    }
                }
            },
            "Education": {
                "type": "nested",
                "include_in_parent": true,
                "properties": {
                    "Degree_Type": {
                        "type": "text"
                    },
                    "Faculty": {
                        "type": "text"
                    },
                    "From_Date": {
                        "type": "text"
                    },
                    "GPA": {
                        "type": "float"
                    },
                    "Institute": {
                        "type": "text"
                    },
                    "Qualification": {
                        "type": "text"
                    },
                    "Subject": {
                        "type": "text"
                    },
                    "To_Date": {
                        "type": "text"
                    }
                }
            },
            "Email": {
                "type": "text"
            },
            "Employee_ID": {
                "type": "long"
            },
            "Employee_Name": {
                "type": "text"
            },
            "Image_URL": {
                "type": "text"
            },
            "Join_Date": {
                "type": "text"
            },
            "Languages": {
                "type": "text"
            },
            "MD": {
                "type": "text"
            },
            "Past_Projects": {
                "type": "nested",
                "include_in_parent": true,
                "properties": {
                    "From": {
                        "type": "text"
                    },
                    "Project_ID": {
                        "type": "text"
                    },
                    "Project_Name": {
                        "type": "text"
                    },
                    "To": {
                        "type": "text"
                    }
                }
            },
            "Position": {
                "type": "text"
            },
            "Project_Role": {
                "type": "text"
            },
            "Skills": {
                "type": "text"
            },
            "Telephone": {
                "type": "long"
            },
            "Training_Courses": {
                "type": "nested",
                "include_in_parent": true,
                "properties": {
                    "Course_Status": {
                        "type": "text"
                    },
                    "First_Training_Date": {
                        "type": "text"
                    },
                    "Training_Course": {
                        "type": "text"
                    },
                    "Year": {
                        "type": "long"
                    }
                }
            }
        }
    }
}'''


projects_mapping = '''
{
    "mappings": {
        "properties": {
            "Project_Name": {
                "type": "text"
            },

            "Status": {
                "type": "text"
            },

            "People": {
                "type": "nested",
                "include_in_parent": true,
                "properties": {
                    "Employee_ID": {
                        "type": "keyword"
                    },
                    "Employee_Name": {
                        "type": "text"
                    }
                }
            }
        }
    }
}'''

skills_mapping = '''
{
    "mappings": {
        "properties": {
            "Skill": {
                "type": "text"
            },
            "People": {
                "type": "nested",
                "include_in_parent": true,
                "properties": {
                    "Employee_ID": {
                        "type": "keyword"
                    },
                    "Employee_Name": {
                        "type": "text"
                    }
                }
            }
        }
    }
}'''
