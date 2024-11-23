#!/usr/bin/env python
###########################################################################################
#
# Author: Daniel Tehan
#
# Date: Nov 3, 2024
#
# Required packagages: python 3.11, teradataml, crewai, crewai-tools, langchain_aws
#
#
###########################################################################################
import asyncio
from pydantic import BaseModel
from crewai.flow.flow import Flow, listen, start, or_, router
from typing import List
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
)

# Application libraries
from databases.database import Database
from util.helper import get_crew_type
from util.helper import get_crew
from util.db_credentials import get_credentials
# Database table description crews
from crews.writer_crew.openai_writer_crew import OpenAIWriterCrew
from crews.writer_crew.bedrock_writer_crew import BedrockWriterCrew
from crews.writer_crew.azure_writer_crew import AzureWriterCrew
# Database Great Expectation crews
from crews.expectation_crew.openai_expectation_crew import OpenAIExpectationCrew
from crews.expectation_crew.bedrock_expectation_crew import BedrockExpectationCrew
from crews.expectation_crew.azure_expectation_crew import AzureExpectationCrew


class ExpectationState(BaseModel):
    db_type: str = ""
    host: str = ""
    user: str = ""
    password: str = ""
    port: str = ""
    logmech: str = ""
    schema_name: str = ""
    all_tables: List[str] = []
    all_tables_input_str: List[str] = []
    all_tables_output_str: List[str] = []


class ExpectationFlow(Flow[ExpectationState]):

    crew_type = get_crew_type()

    @start()
    def get_credentials(self):
        print("#################################")
        print("Gathering database credentials...")

        # Get database credentials from user
        credentials = get_credentials()
        if len(credentials) == 7:
            self.state.db_type, self.state.schema_name, self.state.host, self.state.port, self.state.user, self.state.password, self.state.logmech = credentials
        else:
            print("Failed to retrieve credentials from prompt.")

    @listen(get_credentials)
    def make_connection(self):
        print("#################################")
        print(f"Connecting to {self.state.db_type} .........")

        # Connects to database
        my_db = Database(self.state.db_type, self.state.host, self.state.schema_name,
                         self.state.user, self.state.password, self.state.port, self.state.logmech)
        db = my_db.get_database()
        print(f"Connection to {self.state.db_type} successful.")
        return db

    @listen(make_connection)
    def get_all_tables(self, db):
        print("#################################")
        print(f"Retrieving all tables from {self.state.schema_name} --")

        # Gets list of tables in database scema
        tablesString = ListSQLDatabaseTool(db=db).invoke("")
        self.state.all_tables = tablesString.split(",")
        # cleans up table names into a list of strings
        for i in range(len(self.state.all_tables)):
            self.state.all_tables[i] = self.state.all_tables[i].strip()
        return db

    @listen(get_all_tables)
    def get_table_info(self, db):
        print("#################################")
        print("Getting table info")

        # Cycles through list of tables, gets create table and sample rows
        for i in range(len(self.state.all_tables)):
            self.state.all_tables_input_str.append(
                InfoSQLDatabaseTool(db=db).invoke(self.state.all_tables[i]))

    @router(get_table_info)
    def routing_to_crew_type(self):
        return self.crew_type

    @listen(or_("Bedrock-Sonet", "Bedrock-Llama"))
    def get_table_description_bedrock(self):
        print("#################################")
        print("Getting table description Bedrock")

        if get_crew() == "writer":
            bedrockWriterCrew = BedrockWriterCrew()
        if get_crew() == "expectation":
            bedrockExpectationCrew = BedrockExpectationCrew()
        # Cycles through list of tables, gets a short description of the table
        for i in range(len(self.state.all_tables)):
            input = {'table_definition': self.state.all_tables_input_str[i]}
            if get_crew() == "writer":
                writer_result = bedrockWriterCrew.kickoff(inputs=input)
                self.state.all_tables_output_str.append(writer_result)
            if get_crew() == "expectation":
                expectation_result = bedrockExpectationCrew.kickoff(
                    inputs=input)
                self.state.all_tables_output_str.append(expectation_result)

    @listen("OpenAI")
    def get_table_description_openai(self):
        print("#################################")
        print("Getting table description OpenAI")

        if get_crew() == "writer":
            openAIWriterCrew = OpenAIWriterCrew()
        if get_crew() == "expectation":
            openAIExpectationCrew = OpenAIExpectationCrew()
        # Cycles through list of tables, gets a short description of the table
        for i in range(len(self.state.all_tables)):
            input = {'table_definition': self.state.all_tables_input_str[i]}
            if get_crew() == "writer":
                writer_result = openAIWriterCrew.crew().kickoff(inputs=input)
                self.state.all_tables_output_str.append(writer_result.raw)
            if get_crew() == "expectation":
                expectation_result = openAIExpectationCrew.crew().kickoff(inputs=input)
                self.state.all_tables_output_str.append(expectation_result.raw)

    @listen("Azure-GPT")
    def get_table_description_azure(self):
        print("#################################")
        print("Getting table description Azure")

        if get_crew() == "writer":
            azureWriterCrew = AzureWriterCrew()
        if get_crew() == "expectation":
            azureExpectationCrew = AzureExpectationCrew()
        # Cycles through list of tables, gets a short description of the table
        for i in range(len(self.state.all_tables)):
            input = {'table_definition': self.state.all_tables_input_str[i]}
            if get_crew() == "writer":
                writer_result = azureWriterCrew.kickoff(inputs=input)
                self.state.all_tables_output_str.append(writer_result)
            if get_crew() == "expectation":
                expectation_result = azureExpectationCrew.kickoff(inputs=input)
                self.state.all_tables_output_str.append(expectation_result)

    @listen(or_(get_table_description_bedrock, get_table_description_openai, get_table_description_azure))
    def build_table_report(self):
        print("#################################")
        print("Building table report")

        if get_crew() == "writer":
            # Add the report intro
            script = f"# Table report for {self.state.schema_name} schema.\n\n"

            # Cycle thru the tables adding them to the report
            for i in range(len(self.state.all_tables)):
                script = script + "## Table Name: " + \
                    self.state.all_tables[i] + "\n\n"
                script = script + \
                    self.state.all_tables_output_str[i] + "\n\n\n"

            # write the script to a file
            print("#################################")
            print("writting the report")
            f = open(
                f"crews/writer_crew/Output/{self.state.schema_name}_{self.crew_type}_Schema_Report.md", "w")
            f.write(script)
            f.close()

        if get_crew() == "expectation":
            # Add the script intro
            script = f"# This script build the great expectations config for the {self.state.schema_name}.\n"
            # add the begining part of the script
            string = open(
                "crews/expectation_crew/config/pre_script.txt", "r").read()
            conn_str = f"{self.state.db_type}://{self.state.user}:{self.state.password}@{self.state.host}:{self.state.port}/{self.state.schema_name}?logmech={self.state.logmech}"
            string = string.replace("conn_str", conn_str)
            string = string.replace("dsname", self.state.db_type)
            string = string.replace("schema_name", self.state.schema_name)
            script = script + string + "\n"
            # add the expectations part of the script
            for i in range(len(self.state.all_tables)):
                self.state.all_tables_output_str[i] = self.state.all_tables_output_str[i].replace(
                    "```python", "\n")
                self.state.all_tables_output_str[i] = self.state.all_tables_output_str[i].replace(
                    "```", "\n")
                script = script + \
                    self.state.all_tables_output_str[i] + "\n\n\n"

            # add the closing part of the script
            script = script + \
                open("crews/expectation_crew/config/post_script.txt",
                     "r").read() + "\n"

            # write the script to a file
            print("#################################")
            print("writting the great expectation script")
            f = open(
                f"crews/expectation_crew/Output/{self.state.schema_name}_{self.crew_type}_script.py", "w")
            f.write(script)
            f.close()


if __name__ == "__main__":
    expectation_flow = ExpectationFlow()
    expectation_flow.kickoff()
