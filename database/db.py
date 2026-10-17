

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


#db url
DATABASE_URL = "sqlite:///database/projects.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
