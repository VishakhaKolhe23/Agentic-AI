# middleware.py

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# State
class AgentState(TypedDict):
    user_input: str
    response: str

# Middleware
def middleware(state: AgentState):
    """
    Runs before main agent logic.
    Used for:
    - Logging
    - Authentication
    - Input filtering
    """

    print(f"[Middleware] User Input: {state['user_input']}")

    blocked_words = ["hack", "password"]

    for word in blocked_words:
        if word in state["user_input"].lower():
            return {
                "response": "Blocked by middleware: Unsafe request detected."
            }

    return {}


# Main Agent
def agent_node(state: AgentState):
    return {
        "response": f"Agent processed: {state['user_input']}"
    }



# Build Graph

graph = StateGraph(AgentState)

graph.add_node("middleware", middleware)
graph.add_node("agent", agent_node)

graph.add_edge(START, "middleware")
graph.add_edge("middleware", "agent")
graph.add_edge("agent", END)

app = graph.compile()


#run
if __name__ == "__main__":

    result = app.invoke(
        {"user_input": "Tell me about RAG"}
    )

    print(result["response"])