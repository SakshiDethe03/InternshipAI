from app.schemas.resume import Resume
from app.data.internships import internships
from app.nodes.eligibility import check_eligibility
from graph.internship_graph import graph


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

initial_state = {"resume": resume}

result = graph.invoke(initial_state)

print("\n=============================")
print("FINAL RESULT")
print("===============================")

print("Submitted Applications:")
print(result.get("submitted_applications", {}))
