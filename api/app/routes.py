from fastapi import APIRouter, HTTPException

from .schema import ConditionCount
from .service import get_condition_counts

router = APIRouter(prefix="/api")


@router.get("/condition_counts", response_model=list[ConditionCount])
def read_condition_counts():
    """
    Endpoint to fetch the count of conditions grouped by gender and condition
    description from the Databricks SQL database.
    Returns:
        List[ConditionCount]: A list of ConditionCount objects containing the gender,
        condition description, and the count of each condition.
    """
    condition_counts = get_condition_counts()

    if condition_counts is None:
        raise HTTPException(
            status_code=500, detail="Error fetching condition counts from the database."
        )

    return condition_counts
