import json
import uuid
from schemas.resume import Resume
from schemas.internship import Internship
from schemas.JD_matching import JDMatchingResult
from schemas.application_schema import ApplicationData

from llm.llm_helper import llm
from prompt.application_writer_prompt import PROMPT


def write_application(
    resume: Resume,
    internship: Internship,
    jd_match: JDMatchingResult,
) -> ApplicationData:

    application_id = f"APP-{uuid.uuid4().hex[:8]}"

    # Build the prompt using information already available
    # from the resume, internship, and JD matching analysis.
    prompt = PROMPT.format(
        resume=json.dumps(resume.model_dump()),
        internship=json.dumps(internship.model_dump()),
        jd_match=json.dumps(jd_match.model_dump()),
    )

    # Ask the LLM to generate the tailored application content.
    response = llm.invoke(prompt)

    # Extract the text returned by the LLM.
    result = response.content.strip()

    # Convert the JSON string into a Python dictionary.
    data = json.loads(result)

    # Keep factual candidate and internship information directly
    # from validated objects instead of asking the LLM to generate it.
    application = ApplicationData(
        application_id=application_id,
        internship_id=internship.internship_id,
        status="AWAITING APPROVAL",
        name=resume.name,
        email=resume.email,
        phone=resume.phone,
        linkedin=resume.linkedin,
        github=resume.github,
        resume=data["resume"],
        cover_letter=data["cover_letter"],
        answers=data["answers"],
    )

    return application
