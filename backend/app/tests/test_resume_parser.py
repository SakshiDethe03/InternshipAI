from tools.resume_parser import extract_resume_text

file_path = "C:/Users/SAKSHI/Desktop/AI/Resume/AIML/SakshiDethe-AIML.pdf"

text = extract_resume_text(file_path)

print("==================EXTRACTED RESUME====================")
print(text)
