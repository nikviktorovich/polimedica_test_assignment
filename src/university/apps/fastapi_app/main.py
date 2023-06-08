import logging

import fastapi
import fastapi.responses
from fastapi import status

import university.common.errors
import university.apps.fastapi_app.routers.courses


logger = logging.getLogger(__name__)
app = fastapi.FastAPI()


@app.exception_handler(university.common.errors.EntityNotFoundError)
def not_found_error_handler(
    request: fastapi.Request,
    exception: university.common.errors.EntityNotFoundError,
):
    return fastapi.responses.JSONResponse(
        content=str(exception),
        status_code=status.HTTP_404_NOT_FOUND,
    )


@app.exception_handler(Exception)
def global_exception_handler(request: fastapi.Request, exception: Exception):
    logger.error(str(exception), exc_info=True)
    return fastapi.responses.JSONResponse(
        content='Server error',
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


app.include_router(university.apps.fastapi_app.routers.courses.router)