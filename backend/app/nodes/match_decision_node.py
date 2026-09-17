from state.agent_state import AIApplicationAgentState
from nodes.match_decision import make_match_decision


def match_decision_node(state: AIApplicationAgentState):

    internships = state["internships"]

    eligibility_results = state["eligibility_results"]
    jd_matching_results = state["jd_matching_results"]

    match_decisions = {}

    for internship in internships:

        match_decision = make_match_decision(
            eligibility_results[internship.internship_id],
            jd_matching_results[internship.internship_id],
        )
        match_decisions[internship.internship_id] = match_decision

    return {"match_decisions": match_decisions}
