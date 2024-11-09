
###########################################################################################
#
# Author: Daniel Tehan
#
# Date: Nov 3, 2024
#
#
#
###########################################################################################

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from util.helper import get_openai_model


@CrewBase
class OpenAIWriterCrew():

    def __init__(self):
        self.agents_config = 'config/agents.yaml'
        self.tasks_config = 'config/tasks.yaml'
        print("########### Getting LLM ############")
        self.llm = get_openai_model()

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            llm=self.llm,
        )

    @task
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['writer_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=False,
        )
