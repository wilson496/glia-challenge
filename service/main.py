from fastapi import FastAPI


# from pydantic import BaseModel

from service.config import API_V1_STR, PROJECT_NAME
from service.api.jumble_audit import router as api_router

app = FastAPI()

app.include_router(api_router, prefix=API_V1_STR)


@app.get("/health", summary="Check that the service is operational")
def health():
    """
    Sanity check - this will let the user know that the service is operational.
    It is also used as part of the HEALTHCHECK. Docker uses curl to check that the API service is still running, by exercising this endpoint.
    """
    return {"status": "OK"}
