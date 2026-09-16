import json

try:
    from schemas.resume import Resume
    from schemas.internship import Internship
    from schemas.JD_matching import JDMatchingResult
    from llm.llm_helper import llm
    from tools.skill_matching import match_skills
except ModuleNotFoundError:
    from app.schemas.resume import Resume
    from app.schemas.internship import Internship
    from app.schemas.JD_matching import JDMatchingResult
    from app.llm.llm_helper import llm
    from app.tools.skill_matching import match_skills


def match_resume_to_jd(resume: Resume, internship: Internship) -> JDMatchingResult:

    # ---------------------------------------------------------
    # STEP 1: Deterministic skill matching using Python
    # ---------------------------------------------------------

    matched_skills, missing_skills = match_skills(
        resume.skills, internship.requirements
    )

    # Calculate objective match score.
    if internship.requirements:
        match_score = (len(matched_skills) / len(internship.requirements)) * 100
    else:
        match_score = 0

    # ---------------------------------------------------------
    # STEP 2: Ask LLM for qualitative analysis
    # ---------------------------------------------------------

    prompt = f"""
You are an internship resume analysis assistant.

Analyze the candidate's project experience and overall relevance
to the internship.

Candidate:
Role: {resume.role}
Skills: {resume.skills}
Projects: {resume.projects}
Experience: {resume.experience}
Summary: {resume.summary}

Internship:
Role: {internship.role}
Description: {internship.description}
Requirements: {internship.requirements}

The following skill matching has already been calculated
by the application and must NOT be changed:

Matched skills:
{matched_skills}

Missing skills:
{missing_skills}

Match score:
{match_score}

Your job is ONLY to provide qualitative analysis.

Analyze:
1. How relevant the candidate's projects are to this internship.
2. What the candidate's main strengths are.
3. Give a short overall summary.

Return ONLY valid JSON in exactly this format:

{{
    "strengths": [
        "strength 1",
        "strength 2",
        "strength 3"
    ],
    "summary": "short overall summary"
}}

Rules:
- strengths must be a list of strings.
- summary must be a string.
- Do not calculate or change the match score.
- Do not change matched_skills.
- Do not change missing_skills.
- Do not include Markdown.
- Do not include explanations outside the JSON.
"""

    result = llm.invoke(prompt)

    print("RAW LLM RESPONSE:")
    print(repr(result.content))

    # ---------------------------------------------------------
    # STEP 3: Clean LLM JSON response
    # ---------------------------------------------------------

    content = result.content.strip()

    if content.startswith("```json"):
        content = content[7:]

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    data = json.loads(content)

    # ---------------------------------------------------------
    # STEP 4: Build final structured result
    # ---------------------------------------------------------

    return JDMatchingResult(
        match_score=match_score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        strengths=data["strengths"],
        summary=data["summary"],
    )
