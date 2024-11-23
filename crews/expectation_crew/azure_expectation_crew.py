###########################################################################################
#
# Author: Daniel Tehan
#
# Date: Nov 23, 2024
#
#
#
###########################################################################################
import os
import openai
import yaml
from util.helper import load_env


class AzureExpectationCrew():
    agents_path = 'crews/expectation_crew/config/agents.yaml'
    tasks_path = 'crews/expectation_crew/config/tasks.yaml'
    max_tokens = 20000

    def __init__(self):
        load_env()
        # Change the following to False if a role switch is not required

        self.azure_client = openai.AzureOpenAI(
            api_version=os.getenv("azure_api_version"),
            azure_endpoint=os.getenv("azure_endpoint"),
            api_key=os.getenv("azure_api_key")
        )

        # Get prompt information from yaml files
        self.agents_config = yaml.safe_load(open(self.agents_path, 'r'))
        self.tasks_config = yaml.safe_load(open(self.tasks_path, 'r'))

        # Get model infomation
        self.crew_type = os.getenv("crew_type")
        if self.crew_type == "Azure-GPT":
            self.model_id = os.getenv("azure_model_gpt-4o-mini")

    def kickoff(self, inputs):
        # Building the system prompt and messages for the bedrock model
        system_prompt = "You are a " + self.agents_config['expectation_writer']['role'] + " who will " + \
            self.agents_config['expectation_writer']['goal'] + \
            self.agents_config['expectation_writer']['backstory']

        # Building the user prompt
        prompt_data = self.tasks_config['write_expectation']['description'] + \
            " Expected output will be: " + \
            self.tasks_config['write_expectation']['expected_output']
        for key, value in inputs.items():
            prompt_data = prompt_data.replace(key, value)
        user_message = {"role": "user", "content": prompt_data}
        messages = [user_message]

        response = self.azure_client.chat.completions.create(
            model=self.model_id,
            messages=messages
        )

        return response.model_dump()['choices'][0]['message']['content']
