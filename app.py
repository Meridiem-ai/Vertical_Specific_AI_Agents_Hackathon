from fastapi import FastAPI, Body

# Import the main function
from main import main_

# Create FastAPI instance
app = FastAPI()

# Define an endpoint to run the main function
@app.post("/run-agent/")
async def run_agent_endpoint(query: str = Body(..., embed=True)):
    # Call the main function with the query parameter
    resp = main_(query)
    return {"output": resp}

# Run FastAPI with 'uvicorn' for local testing
# Run the command: uvicorn fastapi_agent_runner:app --reload
