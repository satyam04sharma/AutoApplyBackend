# configAPI.py

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from pathlib import Path
import yaml
import os

# Define the data folder path
data_folder = Path( os.getcwd()+"/data_folder_example")

# Define a Pydantic model for the configuration settings
class Config(BaseModel):
    secrets: dict
    config: dict
    plain_text_resume: dict

# Create a FastAPI router
config_api = APIRouter()
# GET /config: Returns the current configuration settings
@config_api.get("/config")
async def get_config():
    try:
        secrets_path = data_folder / "secrets.yaml"
        config_path = data_folder / "config.yaml"
        plain_text_resume_path = data_folder / "plain_text_resume.yaml"

        with open(secrets_path, "r") as f:
            secrets = yaml.safe_load(f)

        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        with open(plain_text_resume_path, "r") as f:
            plain_text_resume = yaml.safe_load(f)

        return Config(secrets=secrets, config=config, plain_text_resume=plain_text_resume)
    except yaml.YAMLError as e:
        return {"error": f"YAML parsing error: {str(e)}"}
    except FileNotFoundError:
        return {"error": "Configuration files not found"+str(secrets_path)}

# POST /config: Updates the configuration settings
@config_api.post("/config")
async def update_config(config: Config):
    try:
        secrets_path = data_folder / "secrets.yaml"
        config_path = data_folder / "config.yaml"
        plain_text_resume_path = data_folder / "plain_text_resume.yaml"

        with open(secrets_path, "w") as f:
            yaml.dump(config.secrets, f)

        with open(config_path, "w") as f:
            yaml.dump(config.config, f)

        with open(plain_text_resume_path, "w") as f:
            yaml.dump(config.plain_text_resume, f)

        return {"message": "Configuration updated successfully"}
    except yaml.YAMLError as e:
        return {"error": f"YAML parsing error: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}

# GET /config/secrets: Returns the secrets.yaml file contents
@config_api.get("/config/secrets")
async def get_secrets():
    try:
        secrets_path = data_folder / "secrets.yaml"
        with open(secrets_path, "r") as f:
            secrets = yaml.safe_load(f)
        return secrets
    except yaml.YAMLError as e:
        return {"error": f"YAML parsing error: {str(e)}"}
    except FileNotFoundError:
        return {"error": "Secrets file not found"}

# POST /config/secrets: Updates the secrets.yaml file contents
@config_api.post("/config/secrets")
async def update_secrets(secrets: dict):
    try:
        secrets_path = data_folder / "secrets.yaml"
        with open(secrets_path, "w") as f:
            yaml.dump(secrets, f)
        return {"message": "Secrets updated successfully"}
    except Exception as e:
        return {"error": str(e)}

# GET /config/config: Returns the config.yaml file contents
@config_api.get("/config/config")
async def get_config_yaml():
    try:
        config_path = data_folder / "config.yaml"
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        return config
    except yaml.YAMLError as e:
        return {"error": f"YAML parsing error: {str(e)}"}
    except FileNotFoundError:
        return {"error": "Config file not found"}

# POST /config/config: Updates the config.yaml file contents
@config_api.post("/config/config")
async def update_config_yaml(config: dict):
    try:
        config_path = data_folder / "config.yaml"
        with open(config_path, "w") as f:
            yaml.dump(config, f)
        return {"message": "Config updated successfully"}
    except yaml.YAMLError as e:
        return {"error": f"YAML parsing error: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}

# GET /config/plain_text_resume: Returns the plain_text_resume.yaml file contents
@config_api.get("/config/plain_text_resume")
async def get_plain_text_resume():
    try:
        plain_text_resume_path = data_folder / "plain_text_resume.yaml"
        with open(plain_text_resume_path, "r") as f:
            plain_text_resume = yaml.safe_load(f)
        return plain_text_resume
    except yaml.YAMLError as e:
        return {"error": f"YAML parsing error: {str(e)}"}
    except FileNotFoundError:
        return {"error": "Plain text resume file not found"}

# POST /config/plain_text_resume: Updates the plain_text_resume.yaml file contents
@config_api.post("/config/plain_text_resume")
async def update_plain_text_resume(plain_text_resume: dict):
    try:
        plain_text_resume_path = data_folder / "plain_text_resume.yaml"
        with open(plain_text_resume_path, "w") as f:
            yaml.dump(plain_text_resume, f)
        return {"message": "Plain text resume updated successfully"}
    except yaml.YAMLError as e:
        return {"error": f"YAML parsing error: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}