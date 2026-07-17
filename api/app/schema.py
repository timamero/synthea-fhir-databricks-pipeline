from pydantic import BaseModel


# ConditionCount model for API response
class ConditionCount(BaseModel):
    gender: str
    condition_description: str
    condition_count: int
