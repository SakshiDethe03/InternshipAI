try:
    from schemas.eligibility import EligibilityResult
    from schemas.JD_matching import JDMatchingResult
    from schemas.match_decision import MatchDecisionResult
except ModuleNotFoundError:
    from app.schemas.eligibility import EligibilityResult
    from app.schemas.JD_matching import JDMatchingResult
    from app.schemas.match_decision import MatchDecisionResult


def make_match_decision(
    eligibility: EligibilityResult, jd_match: JDMatchingResult
) -> MatchDecisionResult:

    # --------------------------------------
    # Step 1: Check the eligibility
    # --------------------------------------

    if not eligibility.is_eligible:
        return MatchDecisionResult(
            should_continue=False, category="Not eligible", reason=eligibility.feedback or "Not eligible"
        )

    # --------------------------------------
    # Step 2: Categorize the JD match
    # --------------------------------------

    score = jd_match.match_score

    if score >= 90:
        category = "Strong Match"

    elif score >= 70:
        category = "Good Match"

    elif score >= 50:
        category = "Potential Match"

    else:
        category = "Weak Match"

    # --------------------------------------
    # Step 3: Decide whether to continue
    # --------------------------------------

    if score >= 50:
        should_continue = True

        reason = (
            f"Candidate is eligible and has a {score:.0f}% JD Match. "
            f"The candidate can continue to application preparation."
        )

    else:
        should_continue = False

        reason = (
            f"Candidate is eligible but has a {score:.0f}% JD Match. "
            f"The match is currently too weak to continue automatically."
        )

    return MatchDecisionResult(
        should_continue=should_continue, category=category, reason=reason
    )
