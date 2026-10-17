

from datetime import date, time

from sqlalchemy import(
    String,
    Text,
    ForeignKey,
    Date,
    Time,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.db import Base


class School(Base):
    __tablename__ = "schools"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    
    school_name: Mapped[str] = mapped_column(String(150), nullable=False)
    num_of_classes: Mapped[int] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(String(300), nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    
    

    