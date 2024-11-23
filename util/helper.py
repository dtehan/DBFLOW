###########################################################################################
#
# Author: Daniel Tehan
#
# Date: Nov 3, 2024
#
#
#
###########################################################################################

import os
from dotenv import load_dotenv, find_dotenv
from crewai import LLM


def load_env():
    _ = load_dotenv(find_dotenv('geflow.env'))


def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key


def get_openai_model_name():
    load_env()
    model_name = os.getenv("OPENAI_MODEL")
    return model_name


def get_dbconfig_file_path():
    load_env()
    dbconfig_file_path = os.getenv("DBConfigFilePath")
    return dbconfig_file_path


def get_openai_model():
    openai_llm = LLM(
        model=get_openai_model_name(),
        api_key=get_openai_api_key()
    )
    return openai_llm


def get_crew_type():
    load_env()
    return os.getenv("crew_type")


def get_crew():
    load_env()
    return os.getenv("crew")
