from langgraph.graph import StateGraph, START, END

from state.agent_state import AIApplicationAgentState

from tools.search_internships import search_internships
from nodes.search_result_node import (
    search_result_node,
    search_result_router,
)
from nodes.eligibility_node import eligibility_node
from nodes.jd_matching_node import jd_matching_node
from nodes.match_decision_node import match_decision_node
from nodes.application_writer_node import application_writer_node
from nodes.approval_node import approval_node
from nodes.submission_node import submission_node


def search_node(state: AIApplicationAgentState):
    internships = search_internships()

    return {"internships": internships}


def approval_router(state: AIApplicationAgentState):
    """Route the graph based on user approval."""

    approval_status = state["approval_status"]

    for status in approval_status.values():
        if status == "APPROVED":
            return "submit"

    return "end"


builder = StateGraph(AIApplicationAgentState)


# =========================
# Nodes
# =========================

builder.add_node("search", search_node)
builder.add_node("search_result", search_result_node)
builder.add_node("eligibility", eligibility_node)
builder.add_node("jd_matching", jd_matching_node)
builder.add_node("match_decision", match_decision_node)
builder.add_node("application_writer", application_writer_node)
builder.add_node("approval", approval_node)
builder.add_node("submit", submission_node)


# =========================
# Main Flow
# =========================

builder.add_edge(START, "search")
builder.add_edge("search", "search_result")

# =========================
# Search Result Routing
# =========================

builder.add_conditional_edges(
    "search_result",
    search_result_router,
    {
        "found": "eligibility",
        "not_found": END,
    },
)

builder.add_edge("eligibility", "jd_matching")
builder.add_edge("jd_matching", "match_decision")
builder.add_edge("match_decision", "application_writer")
builder.add_edge("application_writer", "approval")


# =========================
# Approval Routing
# =========================

builder.add_conditional_edges(
    "approval",
    approval_router,
    {
        "submit": "submit",
        "end": END,
    },
)


# =========================
# Submission → END
# =========================

builder.add_edge("submit", END)


# =========================
# Compile
# =========================

graph = builder.compile()
