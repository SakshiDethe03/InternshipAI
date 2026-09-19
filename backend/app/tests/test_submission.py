from nodes.submission_node import submission_node
from schemas.application_schema import ApplicationData


def test_submission_node():

    approved_application = ApplicationData(
        application_id="APP-001",
        internship_id="INT001",
        status="AWAITING_APPROVAL",
        name="Sakshi",
        email="sakshi@example.com",
        phone="9876543210",
        linkedin=None,
        github=None,
        resume="Test resume",
        cover_letter="Test cover letter",
        answers={},
    )

    rejected_application = ApplicationData(
        application_id="APP-002",
        internship_id="INT002",
        status="AWAITING_APPROVAL",
        name="Sakshi",
        email="sakshi@example.com",
        phone="9876543210",
        linkedin=None,
        github=None,
        resume="Test resume",
        cover_letter="Test cover letter",
        answers={},
    )

    state = {
        "application_data": {
            "INT001": approved_application,
            "INT002": rejected_application,
        },
        "approval_status": {
            "INT001": "APPROVED",
            "INT002": "REJECTED",
        },
    }

    result = submission_node(state)

    print("\nRESULT:")
    print(result)

    assert "INT001" in result["submitted_applications"]

    assert "INT002" not in result["submitted_applications"]

    submitted = result["submitted_applications"]["INT001"]

    assert submitted.success is True
    assert submitted.status == "SUBMITTED"


if __name__ == "__main__":
    test_submission_node()
