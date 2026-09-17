from state.agent_state import AIApplicationAgentState
from nodes.jd_matching import match_resume_to_jd


def jd_matching_node(state: AIApplicationAgentState):
    resume = state["resume"]
    internships = state["internships"]

    jd_matching_results = {}

    for internship in internships:
        jd_matching_results[internship.internship_id] = match_resume_to_jd(
            resume, internship
        )

    return {"jd_matching_results": jd_matching_results}
