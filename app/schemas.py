from pydantic import BaseModel


class LeadInput(BaseModel):
    total_visits: int
    time_spent_on_website: float
    page_views_per_visit: float
    asymmetrique_activity_score: float
    asymmetrique_profile_score: float
