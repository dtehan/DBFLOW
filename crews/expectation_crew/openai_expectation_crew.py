
###########################################################################################
#
# Author: Daniel Tehan, Wenjie Tehan
#
# Date: Nov 3, 2024
#
# Required packagages: python 3.11, teradataml, crewai, crewai-tools, great_expectations
#
#
###########################################################################################

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from util.helper import get_openai_model


@CrewBase
class OpenAIExpectationCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    llm = get_openai_model()
    print("########### Using OpenAI ############")

    @agent
    def expectation_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['expectation_writer'],
            llm=self.llm,
        )

    @task
    def write_expectation(self) -> Task:
        return Task(
            config=self.tasks_config['write_expectation'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
