from app.tools.skill_matching import match_skills


resume_skills = ["Py", "Generative AI", "LangGraph", "Git"]

requirements = ["Python", "Machine Learning", "GenAI", "Git"]


matched_skills, missing_skills = match_skills(resume_skills, requirements)

print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)
