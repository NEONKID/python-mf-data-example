from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from loguru import logger

from fastapi_advanced.routes import add_routes
from fastapi_advanced.middlewares import add_middlewares
from fastapi_advanced.middlewares.json import RequireJSON
from fastapi_advanced.middlewares.log import LoggerMiddleware
from fastapi_advanced.middlewares.timeheader import TimeHeaderMiddleware
from fastapi_advanced.src.api import memo, label
from fastapi_advanced.src.containers import Container


def create_app(create_db: bool = False):
    logger.info("Initializing Python Micro Framework Data FastAPI Sample App..")

    container = Container()
    container.wire(modules=[memo, label])

    app = FastAPI(
        title="Python Micro Framework Data FastAPI Example Sample API",
        default_response_class=ORJSONResponse,
        version="0.1",
        description="Python Micro Framework Data FastAPI Example Sample API",
        docs_url=None,
        redoc_url=None
    )
    app.container = container
    db = container.db()

    logger.info("Add middlewares..")
    app.add_middleware(CORSMiddleware,
                       allow_origins=container.config.cors().get('origin'),
                       allow_methods=container.config.cors().get('methods'),
                       allow_headers=container.config.cors().get('headers'))
    add_middlewares([RequireJSON, LoggerMiddleware, TimeHeaderMiddleware], app)

    logger.info("Add Routes..")
    add_routes([memo.router, label.router], app)

    @app.on_event("startup")
    async def on_startup():
        logger.info("Starting Python Micro Framework Data FastAPI Sample App..")

        await db.connect()
        if create_db:
            await db.create_database()

        # TODO: startup code

        logger.info("Started Python Micro Framework Data FastAPI Sample App..")

    @app.on_event("shutdown")
    async def on_shutdown():
        logger.info("Stopping Python Micro Framework Data FastAPI Sample App..")

        await db.disconnect()

        # TODO: shutdown code

        logger.info("Stopped Python Micro Framework Data FastAPI Sample App..")

    return app
