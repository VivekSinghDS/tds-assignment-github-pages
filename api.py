from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Sample data with names and marks
import json

# Open and read the JSON file
with open('./q-vercel-python.json', 'r') as file:
    DATA = json.load(file)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; modify as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/api")
async def get_marks(request: Request):
    # Get query parameters
    names = request.query_params.getlist("name")
    
    # Filter data based on requested names
    response_data = [entry for entry in DATA if entry['name'] in names]
    
    return JSONResponse(content=response_data)

# For local testing
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
