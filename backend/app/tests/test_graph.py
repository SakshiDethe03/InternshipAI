from graph.internship_graph import graph
from schemas.resume import Resume

resume = Resume(
    name="Sakshi Dethe",
    email="sakshi@example.com",
    phone="1234567890",
    linkedin="linkedin.com/in/sakshi",
    github="github.com/SakshiDethe03",
    role="AI Engineer",
    experience="Fresher",
    skills=["Python", "Generative AI", "LangGraph", "Git", "SQL", "RAG", "LangChain"],
    projects=["AI Support Agent", "AI Recruitment Agent"],
    summary="Final-year B.Tech student interested in Agentic AI.",
)


initial_state = {"resume": resume}

result = graph.invoke(initial_state)

print("\n========= FINAL STATE =========")

print(result)

print("\n========= INTERNSHIPS FOUND =========")

for internship in result["internships"]:
    print(internship.company, "|", internship.role, "|", internship.posted_at)

print("\n========= ELIGIBILITY RESULTS =========")

for internship_id, eligibility in result["eligibility_results"].items():

    print(
        internship_id,
        "| Eligible:",
        eligibility.is_eligible,
        "| Unmet:",
        eligibility.unmet_requirements,
    )

print("\n============= JD MATCHING RESULTS ==============")

for internship_id, jd_match in result["jd_matching_results"].items():

    print(
        internship_id,
        "| Score:",
        jd_match.match_score,
        "| Matched Skills:",
        jd_match.matched_skills,
        "| Missing Skills:",
        jd_match.missing_skills,
    )

print("\n============= Match Decision Results =============")

for internship_id, decision in result["match_decisions"].items():
    print(
        internship_id,
        "| Should Continue:",
        decision.should_continue,
        "| Category:",
        decision.category,
        "| Reason:",
        decision.reason,
    )

print("\n============= APPLICATION DATA ==============")

for internship_id, application in result["application_data"].items():
    print(application)
