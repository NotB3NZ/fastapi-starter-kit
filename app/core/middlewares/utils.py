from starlette.requests import Request
from starlette.routing import Match


def get_matching_route_path(request: Request) -> str:
    for route in request.app.routes:
        match, child_scope = route.matches(request.scope)
        if match == Match.FULL:
            return route.path
    return request.url.path


def get_path_params(request: Request) -> dict:
    for route in request.app.routes:
        match, child_scope = route.matches(request.scope)
        if match == Match.FULL:
            return child_scope["path_params"]
    return dict()
