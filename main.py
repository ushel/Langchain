import os

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def main():
    print("Hello from langchain!")
    print(os.environ["OPENAI_API_KEY"])


if __name__ == "__main__":
    main()
