# app.py

from fastapi import FastAPI
from api.configAPI import config_api
from api.applyAPI import apply_api

app = FastAPI()

# Register the APIs

app.include_router(config_api, prefix="/configAPI")
app.include_router(apply_api, prefix="/applyAPI")


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)