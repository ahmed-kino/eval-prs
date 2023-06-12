import os

from langchain.agents import create_json_agent
from langchain.agents.agent_toolkits import JsonToolkit
from langchain.llms.openai import OpenAI
from langchain.tools.json.tool import JsonSpec

from src.utils.logger import Logger


class OpenAIClient:
    def __init__(self, openai_api_key):
        self.logger = Logger()
        self.openai = OpenAI(openai_api_key=openai_api_key, temperature=0)

    def json_agent_executor(self, data_dict):
        try:
            json_spec = JsonSpec(dict_=data_dict, max_value_length=4000)
            json_toolkit = JsonToolkit(spec=json_spec)

            return create_json_agent(
                llm=self.openai, toolkit=json_toolkit, verbose=True
            )
        except Exception as e:
            self.logger.error(f"Error occurred. Reason: {e}")
