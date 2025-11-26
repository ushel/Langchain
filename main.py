from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
load_dotenv()

def main():
    print("Hello from langchain-project!")


if __name__ == "__main__":
    main()
