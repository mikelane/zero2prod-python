from starlite import (
    Starlite,
    get,
)


@get('/')
async def health_check() -> dict[str, str]:
    return {'status': 'ok'}


app = Starlite(route_handlers=[health_check])
