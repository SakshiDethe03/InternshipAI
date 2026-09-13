from app.schemas.resume import Resume
from app.schemas.internship import Internship
from app.schemas.eligibility import EligibilityResult


def check_eligibility(resume: Resume, internship: Internship) -> EligibilityResult:

    unmet_requirements = []

    resume_skills = {skill.lower() for skill in resume.skills}

    for requirement in internship.requirements:
        if requirement.lower() not in resume_skills:
            unmet_requirements.append(requirement)

    # Check experience requirement
    if internship.experience:
        if internship.experience.lower() == "fresher":
            if resume.experience and resume.experience.lower() != "fresher":
                unmet_requirements.append("Fresher requirement")

    is_eligible = True

    feedback = (
        "Candidate can apply, but some skills may need improvement."
        if unmet_requirements
        else "Candidate meets the basic internship requirements."
    )

    return EligibilityResult(
        is_eligible=is_eligible,
        feedback=feedback,
        unmet_requirements=unmet_requirements,
    )
