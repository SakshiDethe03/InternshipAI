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

        print("\n================ APPLICATION WRITER DEBUG ================")
        print("Internship:", internship.internship_id)
        print("Company:", internship.company)
        print("Should continue:", decision.should_continue)
        print("Category:", decision.category)
        print("Reason:", decision.reason)

        if not decision.should_continue:
            print("Skipping application for:", internship.internship_id)
            continue

        jd_match = jd_matching_results[internship.internship_id]

        application = write_application(
            resume=resume,
            internship=internship,
            jd_match=jd_match,
        )

        application_data[internship.internship_id] = application

        print("Application created:", application.application_id)

    print("\nApplications created:")
    print(list(application_data.keys()))

    return {"application_data": application_data}
