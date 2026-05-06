
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

@tool
def search(query:str) -> str:
    """
    Tool that searches over internet and returns the result
    Args:
    query : The query to search for
    Returns:
    The search result
    """
    print(f"Searching for: {query}")
    return "Noida temperature is hot"

llama = ChatOllama(temperature=0, model="qwen3:0.6b")
tools = [search]
agent = create_agent(model=llama,tools=tools)

def main():
    print("Hello from    langchain")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Noida")})
    print(result)