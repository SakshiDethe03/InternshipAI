from state.agent_state import AIApplicationAgentState


def search_result_node(state: AIApplicationAgentState):
    """Check whether recent internships were found."""

    internships = state.get("internships", [])

    if not internships:
        return {
            "workflow_status": "NO_INTERNSHIPS_FOUND",
            "workflow_message": "No internships were posted within the last 24 hours.",
        }

    return {
        "workflow_status": "INTERNSHIPS_FOUND",
        "workflow_message": "Recent internships were found successfully.",
    }


def search_result_router(state: AIApplicationAgentState):
    """Route the graph based on internship search results."""

    if state["workflow_status"] == "INTERNSHIPS_FOUND":
        return "found"

    return "not_found"
