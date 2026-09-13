from app.schemas.application_writer_input import ApplicationWriterInput
from app.schemas.application_schema import ApplicationData

# from app.llm.llm import call_openai_llm
# from app.services.cover_letter import generate_cover_letter
# from app.services.resume import generate_resume
# from app.services.jd_matching import match_jd
# from app.services.application import submit_application
# from app.services.application_writer import ApplicationWriter


def auto_apply_to_internship(application_data: ApplicationData) -> dict:
    """Auto-apply for internship"""

    print("Inside auto_apply_to_internship")
