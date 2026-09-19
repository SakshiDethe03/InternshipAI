from graph.internship_graph import graph
from nodes.application_writer_node import application_writer_node
from schemas.resume import Resume


resume = Resume(
    name="Sakshi Dethe",
    email="sakshi@example.com",
    phone="1234567890",
    linkedin="linkedin.com/in/sakshi",
    github="github.com/SakshiDethe03",
    role="AI Engineer",
    experience="Fresher",
    skills=["Python", "Generative AI", "LangGraph", "Git"],
    projects=["AI Support Agent", "AI Recruitment Agent"],
    summary="Final-year B.Tech student interested in Agentic AI.",
)


# Run the existing graph first.
result = graph.invoke({"resume": resume})


# Run the application writer using the state
# produced by the previous graph nodes.
# application_result = application_writer_node(result)


# print("\n========= APPLICATION WRITER RESULT =========")

# for internship_id, application in application_result["application_data"].items():

#     print("\nApplication ID:", application.application_id)
#     print("\nInternship ID:", internship_id)
#     print("Status:", application.status)
#     print("Name:", application.name)
#     print("Email:", application.email)
#     print("Phone:", application.phone)
#     print("LinkedIn:", application.linkedin)
#     print("GitHub:", application.github)

#     print("\nResume:")
#     print(application.resume)

#     print("\nCover Letter:")
#     print(application.cover_letter)

#     print("\nAnswers:")
#     for question, answer in application.answers.items():
#         print("\nQ:", question)
#         print("A:", answer)
