from state.agent_state import AIApplicationAgentState


def approval_node(state: AIApplicationAgentState):

    applications = state["application_data"]

    approval_status = {}

    if not applications:
        raise ValueError("No applications found in state.")

    for internship_id, application in applications.items():

        print("\n============================")
        print("APPLICATION REQUIRES APPROVAL")
        print("\n============================")

        print("Application ID:", application.application_id)
        print("Internship ID:", internship_id)
        print("Status:", application.status)

        print("\n Cover Letter:")
        print(application.cover_letter)

        print("\n Do you want to approve this application?")
        decision = input("Enter YES or NO: ").strip().upper()

        if decision == "YES":
            approval_status[internship_id] = "APPROVED"

        else:
            approval_status[internship_id] = "REJECTED"

    return {"approval_status": approval_status}
