import json
from pathlib import Path

import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.data.mock_api import get_event_data

# Creates the FastAPI app
app = FastAPI(
    title="Paralympics Data Mock API",
    version="1.0.0"
)

# CORS Configuration
# This is crucial to allow your frontend (running on a different port) to fetch data from this backend.
origins = [
    "http://localhost:8000",
    "*"  # Allow all for development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define two routes for the app
@app.get("/all")
def get_all_paralympics_data():
    data = get_event_data()
    return data


@app.get("/")
def root():
    return {"message": "Backend API is running."}


if __name__ == "__main__":
    uvicorn.run("mock_api:app", host="127.0.0.1", port=8000, reload=True)
