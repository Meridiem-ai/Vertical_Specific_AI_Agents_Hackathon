from exa_py import Exa
import os
import json
from dotenv import load_dotenv
from langchain.agents import tool
load_dotenv()

#@tool
def web_search(name: str) -> str:
    """Searches for information about a person on the web.

    Args:
        name (str): The name of the person to search for.

    Returns:
        str: A message describing the results of the search or indicating if no information was found.
    """

    try:

        exa = Exa(api_key=os.getenv("EXA_api_key"))

        result = exa.search_and_contents(
        name,
        type="keyword",
        num_results=5,
        text=True,
        summary={
            "query": f"Write information about {name}"
        }
        )
        response = f"Here is information about {name} :"
        #json_result = json.loads(result)
        for search_result in result.results:
            response += "\n\nTitle : " + search_result.title+ "\nSummary :" + search_result.summary

        return response
    except:
        return "web search failed"
    