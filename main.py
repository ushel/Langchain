
from typing import List, Optional
from pydantic import BaseModel, Field #basemodel -> base class so we can inherit from in order to define structure datastream
                                      #Field class will allow us to add metadata to our models attributes.
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch   # using langchain tool



load_dotenv()
# want to use source pydantic class as nested field in a another pydantic class which we call as agent response.
class Source(BaseModel):
    """Schema for a source used by the agent.

    """
    url:str = Field(description="The url of the source")
    
class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    
    answer:str = Field(description="The agent's answer to query")
    sources:List[Source] = Field(default_factory=list, description="List of sources to generate the answer.")

    
tavily_client = TavilyClient()  # uses TAVILY_API_KEY from env

class TavilySearchInput(BaseModel):
    """Inputs for Tavily web search."""
    query: str = Field(..., description="The search query to send to Tavily")
    max_results: Optional[int] = Field(
        3, description="Maximum number of results to return"
    )

    # 👇 This is what becomes "additionalProperties": false
    model_config = {"extra": "forbid"}  # Pydantic v2
    # If you're on Pydantic v1, use:
    # class Config:
    #     extra = "forbid"


@tool("tavily_web_search", args_schema=TavilySearchInput)
def tavily_web_search(query: str, max_results: int = 3):
    """Search the web using Tavily."""
    return tavily_client.search(query=query, max_results=max_results)
# tavily = TavilyClient()


#using custom tool with help of tavily
# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet

#     Args:
#         query: The query to search for

#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5")
# tools = [search]
# tools = [TavilySearch]
tools = [tavily_web_search]
agent = create_agent(model=llm, tools=tools,response_format=AgentResponse)
def main():
    print("Hello from langchain-project!")
    result = agent.invoke({
    "messages": [
        HumanMessage(
            content=(
                        "search for 3 job posting for an ai engineer in langchain in the bay area on linkedin and list their details"
                    )
            )
        ]
    })
    print(result)


if __name__ == "__main__":
    main()
