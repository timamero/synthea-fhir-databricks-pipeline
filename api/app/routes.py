from fastapi import APIRouter

from .schema import ConditionCount

router = APIRouter(prefix="/api")


@router.get("/condition_counts")
def get_condition_counts():
    # Sample data for demonstration purposes
    sample_data = [
        ConditionCount(
            gender="Male", condition_description="Hypertension", condition_count=150
        ),
        ConditionCount(
            gender="Female", condition_description="Diabetes", condition_count=200
        ),
    ]
    return sample_data

