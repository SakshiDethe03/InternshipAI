from schemas.internship import Internship


internships = [
    Internship(
        internship_id="INT001",
        company="TechNova AI",
        role="AI/ML Intern",
        stipend="₹15,000/month",
        experience="Fresher",
        location="Remote",
        duration="3 months",
        description="Work on generative AI and machine learning applications.",
        requirements=["Python", "Machine Learning", "Generative AI", "Git"],
        posted_at="2026-09-20T10:00:00",
    ),
    Internship(
        internship_id="INT002",
        company="CloudMind",
        role="GenAI Intern",
        stipend="₹20,000/month",
        experience="Fresher",
        location="Bangalore",
        duration="6 months",
        description="Build LLM-powered applications and RAG pipelines.",
        requirements=["Python", "LLMs", "RAG", "LangChain"],
        posted_at="2026-09-20T12:00:00",
    ),
    Internship(
        internship_id="INT003",
        company="DataWorks",
        role="Data Science Intern",
        stipend="₹12,000/month",
        experience="Fresher",
        location="Mumbai",
        duration="3 months",
        description="Analyze datasets and build machine learning models.",
        requirements=["Python", "SQL", "Pandas", "Machine Learning"],
        posted_at="2026-09-18T08:30:00",
    ),
]
