from uuid import uuid4

from src.initializer import app, logger

HEALTH_RESPONSE: dict[str, str] = {"message": "E-Commerce-Ground-Up at your service"}


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Base end point for health checkup

    Returns:
        dict[str, str]: Returns the response containing message
    """
    meta_obj_dict = {"execution_id": str(uuid4())}
    logger.debug(f"Health API hit. Returning response: {HEALTH_RESPONSE}", extra={"meta_obj": meta_obj_dict})

    return HEALTH_RESPONSE
