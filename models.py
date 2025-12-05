# models.py
from pydantic import BaseModel
from typing import List, Optional

class GrantRequest(BaseModel):
    """
    Schema for the data submitted by the user to the Grant Writer AI.
    """
    project_title: str
    project_goal: str
    target_audience: str
    key_activities: List[str]
    budget_request: float
    timeframe_months: int
    existing_text: Optional[str] = None # For revision or continuation
    
class GrantResponse(BaseModel):
    """
    Schema for the generated text returned by the AI.
    """
    generated_section: str
    estimated_tokens: int = 0
