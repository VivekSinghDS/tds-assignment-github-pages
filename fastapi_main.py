from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd 
app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data from CSV


STUDENTS_DATA = pd.read_csv('./q-fastapi.csv')
@app.get("/api")
async def get_students(request: Request):
    # Get 'class' query parameters
    classes = request.query_params.getlist("class")
    
    if classes:
        # Filter students where 'class' matches any of the provided classes
        filtered_data = STUDENTS_DATA[STUDENTS_DATA['class'].isin(classes)]
    else:
        filtered_data = STUDENTS_DATA

    # Convert DataFrame to the expected JSON format
    students_list = filtered_data.to_dict(orient='records')

    return JSONResponse(content={"students": students_list})
