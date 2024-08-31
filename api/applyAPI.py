# applyAPI.py

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from pathlib import Path
import yaml
from src.linkedIn_job_manager import LinkedInJobManager
import os
# Define the data folder path
data_folder = Path(os.getcwd()+"/data_folder_example")

# Define a Pydantic model for the job application
class JobApplication(BaseModel):
    job_id: dict
    resume: dict
    cover_letter: dict

# Create a FastAPI router
apply_api = APIRouter()

# POST /apply: Handles job applications
@apply_api.post("/apply")
async def apply_for_job(job_application: JobApplication):
    try:
        # Create a LinkedInJobManager instance
        job_manager = LinkedInJobManager()
        
        # Apply for the job using the provided job application data
        job_manager.apply_for_job(job_application.job_id, job_application.resume, job_application.cover_letter)
        
        return {"message": "Job application submitted successfully"}
    except Exception as e:
        return {"error": str(e)}

# GET /applications: Returns a list of all job applications submitted
@apply_api.get("/applications")
async def get_applications():
    try:
        # Create a LinkedInJobManager instance
        job_manager = LinkedInJobManager()
        
        # Get the list of job applications
        applications = job_manager.get_applications()
        
        return applications
    except Exception as e:
        return {"error": str(e)}

# GET /applications/{application_id}: Returns the details of a specific job application
@apply_api.get("/applications/{application_id}")
async def get_application(application_id: str):
    try:
        # Create a LinkedInJobManager instance
        job_manager = LinkedInJobManager()
        
        # Get the job application details
        application = job_manager.get_application(application_id)
        
        return application
    except Exception as e:
        return {"error": str(e)}