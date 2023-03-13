import logging

from fastapi import FastAPI
from src.config import config  # noqa: F401

# ----------------------------------------------------------
# Fast API
app: FastAPI = FastAPI()


# ----------------------------------------------------------
logger = logging.getLogger(__name__)
