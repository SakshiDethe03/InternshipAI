from state.agent_state import AIApplicationAgentState
from nodes.eligibility import check_eligibility


def eligibility_node(state: AIApplicationAgentState):

    resume = state["resume"]
    internships = state["internships"]

    eligibility_results = {}

    for internship in internships:

        result = check_eligibility(resume, internship)

        eligibility_results[internship.internship_id] = result

    return {"eligibility_results": eligibility_results}
