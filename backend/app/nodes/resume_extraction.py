import json
from pprint import pprint

try:
    from schemas.resume import Resume
    from llm.llm_helper import llm
except ModuleNotFoundError:
    from app.schemas.resume import Resume
    from app.llm.llm_helper import llm


def extract_resume_data(resume_text: str) -> Resume:
    prompt = f"""
    You are a resume information extraction assistant.
    
    Extract structured information from the resume text below.
    
    Resume: 
    {resume_text}
    
    Return ONLY valid JSON in exactly this format:
    
    {{
        "name":"candidate name",
        "email":"candidate email",
        "phone":"candidate phone or null",
        "linkedin":"LinkedIn URL or null",
        "github":"GitHub URL or null",
        "role":"candidate's target/current role",
        "experience":"experience level or description or null",
        "skills":[
            "skill1",
            "skill2",
        ],
        "projects":[
            "project 1",
            "project 2",
        ],
        "summary":"candidate summary or null"
    }}
    
    Rules:
    - Extract only information present in resume.
    - Do not invent information.
    - If a field is missing, use null.
    - skills must be a list of strings.
    - projects must be a list of strings.
    - Do not include markdown.
    - Do not include explanations outside the JSON.
    """
    result = llm.invoke(prompt)

    print("RAW LLM RESPONSE:")

    pprint(repr(result.content))

    content = result.content.strip()

    # Remove the markdown code fences if the model adds them
    if content.startswith("```json"):
        content = content[7:]

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    data = json.loads(content)

    return Resume.model_validate(data)
