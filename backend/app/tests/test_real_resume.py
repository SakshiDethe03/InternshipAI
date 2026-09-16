from app.tools.resume_parser import extract_resume_text
from app.nodes.resume_extraction import extract_resume_data


file_path = "C:/Users/SAKSHI/Desktop/AI/Resume/AIML/SakshiDethe-AIML.pdf"

# Step 1: Extract raw text
resume_text = extract_resume_text(file_path)

print("\n===== RAW RESUME TEXT =====")
print(resume_text)


# Step 2: Convert raw text into structured Resume
resume = extract_resume_data(resume_text)

print("\n===== STRUCTURED RESUME =====")
print(resume)

print("\nName:", resume.name)
print("Email:", resume.email)
print("Role:", resume.role)
print("Skills:", resume.skills)
print("Projects:", resume.projects)
print("Experience:", resume.experience)
