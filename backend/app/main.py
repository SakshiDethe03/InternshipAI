from app.schemas.resume import Resume
from app.data.internships import internships
from app.nodes.eligibility import check_eligibility


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


internship = internships[0]

result = check_eligibility(resume, internship)

print("Eligible:", result.is_eligible)
print("Feedback:", result.feedback)
print("Unmet requirements:", result.unmet_requirements)
