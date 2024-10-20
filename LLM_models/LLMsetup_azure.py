import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from openai import AzureOpenAI

from dotenv import load_dotenv
load_dotenv()

def llm(temperature=0.7):
    return AzureChatOpenAI(
        model="gpt-4o",
        # openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        openai_api_version = "2024-05-01-preview",
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        # max_tokens=4096,
        
        azure_deployment=os.getenv("AZURE_OPENAI_GPT4O_DEPLOYMENT_NAME"),
        temperature=temperature,
    )

def llm_new(temperature=0.7):
    return AzureChatOpenAI(
        model="gpt-4o",
        # openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        openai_api_version = "2024-02-15-preview",
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        # max_tokens=4096,
        
        azure_deployment="gpt_4o_airgen",
        temperature=temperature,
    )
   
def llm_o1():
    return AzureChatOpenAI(
        model="o1-preview-new",
        # openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        openai_api_version = "2024-09-01-preview",
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        # max_tokens=4096,
        temperature=1,
        azure_deployment="o1-preview",
        # max_completion_tokens = 5000

    )

def llm_o1_mini():
    return AzureChatOpenAI(
        model="o1-mini-new",
        # openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        openai_api_version = "2024-09-01-preview",
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        # max_tokens=4096,
        temperature=1,
        azure_deployment="o1_mini",
        # max_completion_tokens = 5000

    )


# print(llm().invoke("comment vas tu"))


def llm_mini():
    return AzureChatOpenAI(
        model="gpt-4o-mini",
        # openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        openai_api_version = "2024-02-15-preview",
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        # max_tokens=4096,
        
        azure_deployment="gpt-4o-mini",
        temperature=0.7,
    )

def last_output(llm,plan,ginfo):
    memory = ginfo.retrieve_ORCH_mermory()[:]
    agent_plan_simplified = plan.get_simplified_plan()
    main_task = ginfo.get_main_task()
    previous_outputs = plan.get_all_agent_ouputs()
    #print(f"\n\nAB1AB1AB1\n\nMemory : {memory}\n\nPrevious outputs : {previous_outputs}\n\nOrch ID : {ginfo.orch_ID}\n\nChat ID : {ginfo.chat_ID}\n\n")
    if ginfo.user_lang:
        lang = ginfo.user_lang
    else:
        lang = "EN"

    prompt = f"""
    Your are an AI orchestrator controling a multi AI agent system. 
    A human gave you a mission: '{main_task}', you've now finished (succesfully or not) this mission by talking to agents one by one and giving them instructions. 
    You are to craft a brief, conversational message—much like an assistant reporting back to their boss.
    Your message should clearly state whether the mission was successful and include any pertinent details from the mission that would be of interest to the human who assigned it. 
    Aim for a tone that is friendly, warm, and conversational.
    The message should resemble a direct chat conversation, so avoid greetings or sign-offs. 

    By default you should not take into acount what is written between "###", only take it into account when needed.
    ###
    In the case where the task / mission is to give an information / text to the user : As you are writing the final reply, your message should include the demanded information / text. In that case you should look in the outputs from the agents and you can write a longer message if needed. 
    Only do this if the task is centered around giving something to the user and not executing a set of actions.
    ###

    IF THE MAIN TASK IS NOT EXPLICITLY CENTERED AROUND GIVING AN INFORMATION TO THE USER, YOU SHOULD IGNORE THE PROMPT BETWEEN ###

    Examples:
    Example 1: The task is to send an email -> your message should only include if the mail was sent succesfully or not, not the content itself. Reason: The user asked for the mail to be sent and only wants to know if the email was sent or not succesfully. 
    Exemple 2: The task is to find 10 places for an event next week -> your message should include in this case the results of web search agent. Reason: The user asked for information, so the task is only complete if you give him the information.
    Exemple 3: The task is to create a marketing plan -> your message should include the plan written by one of the agents. Reason: The user asked for a plan, for the task to be completed, you should give him the plan by including it in your message.

    Only write your message, nothing else.
    The message should be in this language : {lang}
"""
    memory_text = f"Here is the plan you created to accomplish the task: {agent_plan_simplified} (you already told the human your plan, so no need to reexplain that) \n Here is a summary of the conversation you had with agents to accomplish the task : \n\n"

    # Loop through each message in the list
    for message in memory:
        if isinstance(message, AIMessage):
            memory_text += f"Orchestrator : {message.content}\n"
        elif isinstance(message, HumanMessage):
            memory_text += f"Agent : {message.content}\n"

    memory_text += "\n\nHere are the outputs of all the agents during the run : \n\n"

    for output in previous_outputs:
        memory_text += f"{output} \n"

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=memory_text)
    ]


    return llm.invoke(messages).content


# print(llm().invoke("bonjour comment vas tu").content)

# def llm_gpt4_turbo():
#     return AzureChatOpenAI(
#         model="gpt-4",
#         openai_api_version="0125-Preview",
#         azure_deployment="gpt4_turbo_e_us",
#         openai_api_type="azure",
#         # api_key="azure",
#         api_version="0125-Preview",
#         azure_endpoint="https://openai-eastus-meridiem.openai.azure.com/"
        
#     )
# print(llm_gpt4_turbo())
# print(llm_gpt4_turbo().invoke("bonjour comment vas tu").content)

# def llm_gpt35():
#     return AzureChatOpenAI(
#         # model="gpt-35-turbo",
#         openai_api_version="0301",
#         azure_deployment="gpt35_east_us",
#     )

# # print(llm().invoke("bonjour comment vas tu").content)
# # print(llm_gpt4_turbo().invoke("bonjour comment vas tu").content)
# print(llm_gpt35().invoke("bonjour comment vas tu").content)