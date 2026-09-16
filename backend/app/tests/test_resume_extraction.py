from nodes.resume_extraction import extract_resume_data

resume_text = """
Sakshi Dethe

AI Engineer

Email: sakshi@example.com
Phone: 9876543210
LinkedIn: linkedin.com/in/sakshi
GitHub: github.com/SakshiDethe03

Skills:
Python, Generative AI, LangGraph, Git, SQL

Projects:
AI Recruitment Agent
AI Support Agent
Prompt2FlowAI

Experience:
Fresher

Final-year B.Tech student interested in Agentic AI.
"""

resume = extract_resume_data(resume_text)

print("\n EXTRACTED RESUME:\n")
print(resume.model_dump_json(indent=4))

print("\n Name:", resume.name)
print("Role:", resume.role)
print("Skills:", resume.skills)
print("Projects:", resume.projects)
