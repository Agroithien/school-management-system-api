

import pydantic
from pydantic import BaseModel, Field, computed_field, field_validator, ConfigDict

from typing import Annotated, Literal


SchoolStatus = Literal["active", "closed"]

class CreateSchool(BaseModel):
    
    school_name: str = Field(min_length=1, max_length=150)
    description: str = Field(min_length=1, max_length=150)



    
    
class UpdateSchool(BaseModel):
    
    school_name: str | None = Field(min_length=1, max_length=150)
    description: str | None = Field(min_length=1, max_length=150)
    


class SchoolResponse(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    school_name: str
    description: str