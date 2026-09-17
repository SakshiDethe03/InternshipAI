from app.schemas import match_decision
from app.nodes.jd_matching_node import jd_matching_node
from langgraph.graph import StateGraph, START, END

from state.agent_state import AIApplicationAgentState
from tools.search_internships import search_internships
from nodes.eligibility_node import eligibility_node
from nodes.match_decision_node import match_decision_node
from nodes.application_writer_node import application_writer_node


def search_node(state: AIApplicationAgentState):

    internships = search_internships()

    return {"internships": internships}


builder = StateGraph(AIApplicationAgentState)

# Nodes
builder.add_node("search", search_node)
builder.add_node("eligibility", eligibility_node)
builder.add_node("jd_matching", jd_matching_node)
builder.add_node("match_decision", match_decision_node)
builder.add_node("application_writer", application_writer_node)

# Edges
builder.add_edge(START, "search")
builder.add_edge("search", "eligibility")
builder.add_edge("eligibility", "jd_matching")
builder.add_edge("jd_matching", "match_decision")
builder.add_edge("match_decision", "application_writer")
builder.add_edge("application_writer", END)

graph = builder.compile()
