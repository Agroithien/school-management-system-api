

from fastapi import FastAPI, HTTPException, Response

from schemas.school import School


app = FastAPI(title="school-management-system")


@app.get("/")
def home():
    return {"message": "School Management API is running..."}



# create schools



@app.get("/school/")
def create_school():
    return {"message": "Schools Creation..."}

# create classes

# create Sections for classes


# create students


# create subjets