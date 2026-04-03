from pydantic import BaseModel


class LeadInput(BaseModel):
    total_visits: int
    time_spent_on_website: float
    lead_source: str
