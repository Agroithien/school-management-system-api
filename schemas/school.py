

import pydantic
from pydantic import BaseModel, Field

from typing import Annotated, Literal



class School(BaseModel):
    school_id: Annotated[str, Field(..., description="enter school id...", examples=["SCH001" "SCH002"])]
    






