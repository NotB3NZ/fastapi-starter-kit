from uuid import uuid4

from starlette.types import ASGIApp, Receive, Scope, Send


class RequestIDMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] not in ("http", "websocket"):
            await self.app(scope, receive, send)
            return

        request_id = uuid4().hex
        scope["state"]["request_id"] = request_id
        await self.app(scope, receive, send)
