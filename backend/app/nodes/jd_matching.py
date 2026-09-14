from schemas.resume import Resume
from schemas.internship import Internship
from schemas.JD_matching import JDMatchingResult
from llm.llm_helper import llm


def match_resume_to_jd(resume: Resume, internship: Internship) -> JDMatchingResult:

    structured_llm = llm.with_structured_output(JDMatchingResult)

    prompt = f"""
You are an internship resume matching assistant.

Compare the candidate's resume with the internship.

Candidate:
Skills: {resume.skills}
Projects: {resume.projects}
Experience: {resume.experience}

Internship:
Role: {internship.role}
Description: {internship.description}
Requirements: {internship.requirements}

Analyze:

1. Match between candidate skills and internship requirements.
2. Relevance of candidate projects to the internship.
3. Relevance of candidate experience.
4. Overall suitability.

Give a match score from 0 to 100.

Important:
- matched_skills should contain skills from the internship requirements
  that the candidate actually demonstrates.
- missing_skills should contain required skills that are not clearly
  demonstrated by the candidate.
- strengths should describe relevant candidate strengths.
- summary should briefly explain the overall match.
"""

    result = structured_llm.invoke(prompt)

    return result
