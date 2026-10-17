

import pydantic
from pydantic import BaseModel, Field, computed_field, field_validator, ConfigDict

from typing import Annotated, Literal


SchoolStatus = Literal["active", "closed"]

class CreateSchool(BaseModel):
    
    school_name: str = Field(min_length=1, max_length=150)
    num_of_classes: int = Field(gt=0,)
    location: str = Field(min_length=1, max_length=150)
    description: str = Field(min_length=1, max_length=150)



    
    
class UpdateSchool(BaseModel):
    
    school_name: str | None = Field(default=None, min_length=1, max_length=150)
    num_of_classes: int| None = Field(default=None, gt=0)
    location: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = Field(default=None, min_length=1, max_length=150)
    


class SchoolResponse(BaseModel):
    
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    school_name: str
    num_of_classes: int
    location: str
    description: str