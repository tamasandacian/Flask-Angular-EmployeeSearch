import os

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

############################# CONNECTION TO ELASTICSEARCH LOCALHOST #############################
# username = os.environ.get('ELASTICSEARCH_USERNAME_LOCALHOST')
# password = os.environ.get('ELASTICSEARCH_PASSWORD_LOCALHOST')
# ES_HOST = {"host": "localhost", "port": 9200}
############################# CONNECTION TO CLOUD ELASTICSEARCH #################################
username = os.getenv('ELASTIC_CLOUD_USERNAME')
password = os.getenv('ELASTIC_CLOUD_PASSWORD')
ES_HOST = "REPLACE_THIS_WITH_YOUR_ES_HOST"
#################################################################################################