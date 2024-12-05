# Build a Business Definition for a database schema

Author: Daniel Tehan, Wenjie Tehan
Date: November 2024

## Process
Ensure that the environment variables are set in getflow.env file, this will contain the LLM keys, model name, and database credential location

The entire flow of the process is controlled using crewai flow.
1. Gets the database credentials
2. Connects to the database
3. Gets a list of tables from the schema identifed in the credentials
4. Connects to the database and gets create table definitions and sample of 3 rows of data
5. Connects to a large language model and builds 
    - writer: the business definition report for the tables in the schema in a markup report
    - expectation: builds a great expectation python script for the tables in the schema


## Configuration

**Open AI Version**
- This version requires an Open AI key to be in the geflow.env file. GPT 4o mini is fast, comprehensive and reasonable price.

**Bedrock Sonet version**
- This requires a set of AWS keys to be defined in the geflow.env file.  Sonet 3.5 does a comprehensive job, but is slow and more expensive.

**Bedrock Llama version**
- This requires a set of AWS keys to be defined in the geflow.env file. Llama 3.2 3B or Llama 3.2 1B model is fast and cheap, not a lot of details in the descriptions. 

**Bedrock Nova version**
- This requires a set of AWS keys to be defined in the geflow.env file. Nova Micro and Nova Lite model is fast and cheap. 

**Azure OpenAI version**
- This requires a set of Azure keys to be defined in the geflow.env file. GPT 4o mini is fast, comprehensive and reasonable price.


geflow.env file configuration shown below

```
##################################################
# Application configuration
##################################################
# Crew types supported are: Bedrock-Sonnet, Bedrock-Llama1b, Bedrock-Llama3b, Bedrock-Nova-Micro, Bedrock-Nova-Lite, Azure-GPT, OpenAI
crew_type=Bedrock-Nova-Micro
# Crew types can currently be "writer" - get table defintions OR "expectation" - gets a list of expectations
crew=writer
# DB ConfigFilePath should not be changed
DBConfigFilePath=databases/dbconfig.ini


##################################################
# Open AI key should be inserted below if using OpenAI
##################################################
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini


##################################################
# AWS keys should be inserted below if using Bedrock-Sonet or Bedrock-Llama
##################################################

aws_access_key_id=
aws_secret_access_key=
aws_session_token=

# AWS region should be selected
aws_region=us-east-1
# Used to Swith to another AWS role, if this is not used change aws_role_switch=False
aws_role_switch=True
aws_role_arn=arn:aws:iam::300917836544:role/bedrock_sso
aws_role_name=ben
# Models supported, do not change
aws_model_sonet=anthropic.claude-3-5-sonnet-20240620-v1:0
aws_model_llama3b=us.meta.llama3-2-3b-instruct-v1:0
aws_model_llama1b=us.meta.llama3-2-1b-instruct-v1:0
aws_model_nova_micro=amazon.nova-micro-v1:0
aws_model_nova_lite=amazon.nova-lite-v1:0

##################################################
# Azure keys should be inserted below if using Azure AI
##################################################

azure_api_version=2023-07-01-preview
azure_endpoint=
azure_api_key=
azure_model_gpt-4o-mini=gpt-4o-mini

```

## Database Connection Configuration
This code has been tested with a Teradata database, the code for other databases has been included, but not end to end tested.

The [./databases/dbconfig.ini](./databases/dbconfig.ini) file contains the database connection string, details will be captured on the first run from user input and written to the dbconfig.ini file for subsequent runs.  Contents will look like:
```
[Server]
databasetype = 
host = 
database = 
user = 
password = 
port = 
logmech = 
```

## Directory structure

**Core Directories**

[./](./)
- root directory for the application 
- contains main_bedrock.py & main_openai.py files
- contains geflow.env file

[./databases/](./databases/) 
- contains the databases.py connection code 
- contains the dbconfig.ini file, after the credentials have been collected

[./util/](./util/)
- db_credentials.py gets database credentials from the use the first time
- dbconfig.py writes database config and reads database config file
- helper.py contains functions to read the geflow.env file

**Great Expectation Directories**

[./crews/expectation_crew/](./crews/expectation_crew/)
- bedrock_expectation_crew.py 
- openai_expectation_crew.py
- azure_expectation_crew.py

[./crews/expectation_crew/config/](./crews/expectation_crew/config/)
- agents.yaml contains the agent definition
- tasks.yaml contains the task definition, including prompt
- pre_script.txt, should not be changed
- post_script.txt, should not be changed

[./crews/expectation_crew/Output](./crews/expectation_crew/Output)
- contains the generated great expectation scripts for the schemas, example output is provided

**Database Writer Directories**

[./crews/writer_crew/](./crews/writer_crew/)
- bedrock_writer_crew.py 
- openai_writer_crew.py
- azure_writer_crew.py

[./crews/writer_crew/config/](./crews/writer_crew/config/)
- agents.yaml contains the agent definition
- tasks.yaml contains the task definition, including prompt

[./crews/writer_crew/Output](./crews/writer_crew/Output)
- contains the generated database description for the schemas, example output is provided


## Setup
pip install the following packages into your python3.11 environment
- python 3.11, crewai, crewai-tools, langchain-aws, teradataml, greate_expectations, yaml, openai

**On Linux/Mac:**
```
git clone https://github.com/dtehan/geflow.git
cd geflow
python3.11 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install crewai crewai-tools
pip install teradataml
pip install langchain-aws
pip install great_expectations
pip install yml
pip install openai
source venv/bin/activate
```

**On Windows**
```
git clone https://github.com/Teradata/jaffle_shop_teradata.git
cd geflow
python3.11 -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install crewai crewai-tools
pip install teradataml
pip install langchain-aws
pip install great_expectations
pip install yml
pip install openai
venv\Scripts\activate
```

## Running
**Run this project**
```
venv/bin/python DBFLOW/main.py
```


