from app.schemas.eligibility import EligibilityResult
from app.schemas.JD_matching import JDMatchingResult
from app.nodes.match_decision import make_match_decision

eligibility = EligibilityResult(
    is_eligible=True,
    feedback="Candidate can apply.",
    unmet_requirements=["Machine Learning"],
)

jd_match = JDMatchingResult(
    match_score=75,
    matched_skills=["Python", "GenAI", "Git"],
    missing_skills=["Machine Learning"],
    strengths=["Strong Generative AI project experience", "Good python experience"],
    summary="Candidate has a good overall match.",
)

result = make_match_decision(eligibility, jd_match)

print("Should Continue: ", result.should_continue)
print("Category: ", result.category)
print("Reason: ", result.reason)
