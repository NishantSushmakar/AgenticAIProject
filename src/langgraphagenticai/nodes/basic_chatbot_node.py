from src.langgraphagenticai.state.state import State
from langgraph.graph import StateGraph

class BasicChatbotNode:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def process(self,state:State)->dict:
        print("I am in node")
        return {"messages": self.llm.invoke(state["messages"])}
