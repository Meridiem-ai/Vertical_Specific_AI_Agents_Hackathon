from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

# Import the main function
from main import main_

# Create FastAPI instance
app = FastAPI()

# Enable CORS for all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define an endpoint to run the main function
@app.post("/run-agent/")
async def run_agent_endpoint(query: str = Body(..., embed=True)):
    # Call the main function with the query parameter
    resp = main_(query)
    return {"output": resp}

# Run FastAPI with 'uvicorn' for local testing
# Run the command: uvicorn app:app --reload