from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-oss-20b"
)


class State(TypedDict):

    question: str
    answer: str


def chatbot(state: State):

    response = llm.invoke(
        state["question"]
    )

    return {
        "answer": response.content
    }


graph = StateGraph(State)

graph.add_node("chatbot", chatbot)

graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

app = graph.compile()

result = app.invoke(
    {
        "question": "What is AI?"
    }
)

print(result["answer"])
