""" MAIN EXECUTION FILE"""

from langchain_openai import ChatOpenAI
from LLM_models.LLMsetup_azure import llm_new
from langchain.agents import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from Tools.tool_template import get_word_length
from Tools.outlook import send_email
from Tools.salesforce import add_contact
from Tools.linkedin_axon import send_linkedin_msg
from Tools.web_search import web_search
llm = llm_new()


def run_agent(query,chat_history):
    tools = [add_contact,send_email,web_search,send_linkedin_msg]


    MEMORY_KEY = "chat_history"
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are very powerful assistant, but bad at calculating lengths of words.",
            ),
            MessagesPlaceholder(variable_name=MEMORY_KEY),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    llm_with_tools = llm.bind_tools(tools)

    chat_history = []
    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_tool_messages(
                x["intermediate_steps"]
            ),
            "chat_history": lambda x: x["chat_history"],
        }
        | prompt
        | llm_with_tools
        | OpenAIToolsAgentOutputParser()
    )
    

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


    result = agent_executor.invoke({"input": query, "chat_history": chat_history})
    print(result)
    return result["output"]





def main_(query):
    chat_history = []

    result = run_agent(query,chat_history)
    return result




