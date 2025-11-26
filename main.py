from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
# from tavily import TavilyClient
from langchain_tavily import TavilySearch   # using langchain tool

load_dotenv()

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
tools = [TavilySearch]
agent = create_agent(model = llm, tools=tools)
def main():
    print("Hello from langchain-project!")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job positng for an ai engineer in langchain in the bay area on linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()
