# api.py
import os
import json
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.main import parse_file

# 1. Initialize the FastAPI app
app = FastAPI()

# 2. Add CORS Middleware
# This allows your future frontend to talk to this backend
origins = ["*"]  # For development. Restrict in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Define the root endpoint to check if the API is running
@app.get("/")
def read_root():
    return {"message": "Credit Card Parser API is online."}

# 4. Define the main file parsing endpoint
@app.post("/parse-statement/")
async def parse_statement_endpoint(file: UploadFile = File(...)):
    temp_dir = "temp_api_files"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, file.filename)

    try:
        # Save the uploaded PDF to a temporary file
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Use your existing parsing logic from src/main.py
        output_path = parse_file(temp_path, output_dir="api_output")

        if not output_path:
            raise HTTPException(status_code=400, detail="Could not parse the PDF.")

        # Read the resulting JSON and return it
        with open(output_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    except Exception as e:
        # Catch any unexpected errors during parsing
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    finally:
        # Clean up the temporary directory and its contents
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)