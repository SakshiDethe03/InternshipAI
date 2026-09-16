# Common aliases for skills that can have different names.
SKILL_ALIASES = {
    "genai": "generative ai",
    "generative ai": "generative ai",
    "ml": "machine learning",
    "machine learning": "machine learning",
    "ai": "artificial intelligence",
    "artificial intelligence": "artificial intelligence",
    "python": "py",
    "py": "python",
}


def normalize_skill(skill: str) -> str:
    """
    Normalize a skill for consistent comparison.

    Example:
        "Python" -> "python"
        " PYTHON " -> "python"
        "GenAI" -> "generative ai"
    """

    skill = skill.strip().lower()

    return SKILL_ALIASES.get(skill, skill)


def match_skills(
    resume_skills: list[str], requirements: list[str]
) -> tuple[list[str], list[str]]:

    normalized_resume_skills = {normalize_skill(skill) for skill in resume_skills}

    matched_skills = []
    missing_skills = []

    for requirement in requirements:

        normalized_requirement = normalize_skill(requirement)

        if normalized_requirement in normalized_resume_skills:
            matched_skills.append(requirement)
        else:
            missing_skills.append(requirement)

    return matched_skills, missing_skills
