from dotenv import load_dotenv
load_dotenv()

# from langchainhub import Hub
# from langchainhub import Hub
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
# from langchain.agents.react.agent import create_react_agent
from langchain_classic.agents import create_react_agent
from langchain_tavily import TavilySearch

#argument description and query description is super important for us to be explicit if its ambiguous then llm will have hard time crafting with tool call

tools = [TavilySearch()]


def main():
    print("Hello from langchain-project!")


if __name__ == "__main__":
    main()
