import os

from langchain.agents import create_json_agent
from langchain.agents.agent_toolkits import JsonToolkit
from langchain.llms.openai import OpenAI
from langchain.tools.json.tool import JsonSpec

from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


from src.utils.logger import Logger


class OpenAIClient:
    def __init__(self, openai_api_key):
        self.logger = Logger()
        self.llm = OpenAI(openai_api_key=openai_api_key, temperature=0)
        self.chat = ChatOpenAI(temperature=0)

    def generate_email_template(self, owner, user, commit_url):
        try:
            template = "You are a helpful assistant that generate email for github users."
            system_message_prompt = SystemMessagePromptTemplate.from_template(template)
            human_template = """
            can you generate a better email than the following?
            'Hey {user}, We have noticed that you have made commits such as {commit_url} in this repo.
            Here at org {owner} we are big users of this project and we appreciate the contributions of the maintainers such as yourself.
            We would love to arrange a chat with you if you are interested.'
            """
            human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
            chat_prompt = ChatPromptTemplate.from_messages(
                [system_message_prompt, human_message_prompt]
            )
            chain = LLMChain(llm=self.chat, prompt=chat_prompt)
            return chain.run(user=user, owner=owner, commit_url=commit_url)
        except Exception as e:
            self.logger.error(f"Error occurred. Reason: {e}")

    def json_agent_executor(self, data_dict):
        try:
            json_spec = JsonSpec(dict_=data_dict, max_value_length=4000)
            json_toolkit = JsonToolkit(spec=json_spec)

            return create_json_agent(llm=self.llm, toolkit=json_toolkit, verbose=True)
        except Exception as e:
            self.logger.error(f"Error occurred. Reason: {e}")
