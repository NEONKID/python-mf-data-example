from fastapi import FastAPI
from loguru import logger


def add_routes(routes, app: FastAPI):
    for route in routes:
        app.include_router(route)
        logger.debug("Add route: {}".format(route.prefix))
