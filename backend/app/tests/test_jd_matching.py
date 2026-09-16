from app.schemas.resume import Resume
from app.data.internships import internships
from app.nodes.jd_matching import match_resume_to_jd


resume = Resume(
    name="Sakshi Dethe",
    email="sakshi@example.com",
    phone="1234567890",
    linkedin="linkedin.com/in/sakshi",
    github="github.com/SakshiDethe03",
    role="AI Engineer",
    experience="Fresher",
    skills=["genai", "ml", "python"],
    projects=["AI powered n8n blueprint generator"],
    summary="Final-year B.Tech student interested in Agentic AI.",
)

internship = internships[0]

result = match_resume_to_jd(resume, internship)

print("Match Score:", result.match_score)
print("Matched Skills:", result.matched_skills)
print("Missing Skills:", result.missing_skills)
print("Strengths:", result.strengths)
print("Summary:", result.summary)
