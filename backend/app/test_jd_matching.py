from schemas.resume import Resume
from data.internships import internships
from nodes.jd_matching import match_resume_to_jd


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

result = match_resume_to_jd(resume, internship)

print("Match Score:", result.match_score)
print("Matched Skills:", result.matched_skills)
print("Missing Skills:", result.missing_skills)
print("Strengths:", result.strengths)
print("Summary:", result.summary)
