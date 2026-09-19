from tools.submission_tool import submission_tool
from state.agent_state import AIApplicationAgentState


def submission_node(state: AIApplicationAgentState):
    """This node submits applications to the internship platform."""

    applications = state["application_data"]
    approval_status = state["approval_status"]

    submitted_applications = {}

    for internship_id, status in approval_status.items():

        if status == "APPROVED":
            application = applications[internship_id]

            result = submission_tool(application)

            submitted_applications[internship_id] = result

    return {"submitted_applications": submitted_applications}
