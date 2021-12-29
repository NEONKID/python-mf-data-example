from fastapi import Request
from fastapi.responses import PlainTextResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response


class RequireJSON(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.method in ('POST', 'PUT', 'PATCH') and request.headers.get('content-type') != 'application/json':
            return PlainTextResponse(status_code=415)
        return await call_next(request)
