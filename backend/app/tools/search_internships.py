from datetime import datetime, timedelta

from app.data.internships import internships


def search_internships():
    now = datetime.now()
    cutoff_time = now - timedelta(hours=24)

    print("Current time:", now)
    print("Cutoff time:", cutoff_time)

    for internship in internships:
        posted_time = datetime.fromisoformat(internship.posted_at)

        print(
            internship.company,
            "| Posted:",
            posted_time,
            "| Recent:",
            posted_time >= cutoff_time,
        )

    recent_internships = []

    for internship in internships:
        posted_time = datetime.fromisoformat(internship.posted_at)

        if posted_time >= cutoff_time:
            recent_internships.append(internship)

    return recent_internships
