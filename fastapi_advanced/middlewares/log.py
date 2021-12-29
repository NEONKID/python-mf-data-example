from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, req: Request, call_next: RequestResponseEndpoint) -> Response:
        logger.info('{method}: {end_pnt}'.format(method=req.method, end_pnt=req.url.path))
        res = await call_next(req)
        return res