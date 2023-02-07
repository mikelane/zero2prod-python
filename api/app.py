from pydantic import BaseModel
from starlite import (
    Starlite,
    get,
)

from api.schema.types import StatusMessage


class HealthCheckResponse(BaseModel):
    status: StatusMessage


@get('/health')
async def health_check() -> HealthCheckResponse:
    return HealthCheckResponse(status='ok')


app = Starlite(route_handlers=[health_check])
