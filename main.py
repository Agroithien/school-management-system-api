

from fastapi import FastAPI, HTTPException, Query, Depends

from schemas.school import CreateSchool, UpdateSchool, SchoolResponse

from database.db import Base, engine, get_db
from database.models import School

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine) # this creates base table

app = FastAPI(title="school-management-system")


@app.get("/")
def home():
    return {"message": "School Management API is running..."}




# create schools

@app.post("/school/", response_model=SchoolResponse)
def create_school(school_data: CreateSchool,
                  db: Session = Depends(get_db),
                  ):
    
        
    school = School(**school_data.model_dump()) #unpacking pydantic data
    
    db.add(school)
    db.commit()
    db.refresh(school)
    
    return school

    

# update schools
@app.patch("/school/{school_id}", response_model=SchoolResponse)
def update_school(school_id, db: Session = Depends(get_db), updated_school_data: UpdateSchool):
    
    school = db.get(School, school_id)
    
    if school is None:
        raise HTTPException(status_code=404, detail="school not found please check the school id")
    
    
       
    
    return {"message": "update schools here"}



# list all schools
@app.get("/schools/all", response_model=SchoolResponse)
def list_schools(db: Session = Depends(get_db),):
    return db.query(School).all()



# remove schools
@app.delete("/school/{school_id}")
def remove_school(school_id, db: Session = Depends(get_db)):
    
    school = db.get(School, school_id)
    
    if school is None:
        raise HTTPException(status_code=404, detail="school not found in database")
    
    db.delete(school)
    db.commit()
    
    return school



# create classes

# create Sections for classes


# create students


# create subjets