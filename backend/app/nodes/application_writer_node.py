from state.agent_state import AIApplicationAgentState
from nodes.application_writer import write_application


def application_writer_node(state: AIApplicationAgentState):

    resume = state["resume"]
    internships = state["internships"]

    match_decisions = state["match_decisions"]
    jd_matching_results = state["jd_matching_results"]

    application_data = {}

    for internship in internships:

        decision = match_decisions[internship.internship_id]

        # Skip internships that should not continue
        # to application preparation.
        if not decision.should_continue:
            continue

        jd_match = jd_matching_results[internship.internship_id]

        application = write_application(
            resume=resume,
            internship=internship,
            jd_match=jd_match,
        )

        application_data[internship.internship_id] = application

    return {"application_data": application_data}
