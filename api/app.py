from typing import NewType

from pydantic import BaseModel
from starlite import (
    Starlite,
    get,
)

StatusMessage = NewType('StatusMessage', str)


class HealthCheckResponse(BaseModel):
    status: StatusMessage


@get('/health')
async def health_check() -> HealthCheckResponse:
    return HealthCheckResponse(status='ok')


app = Starlite(route_handlers=[health_check])
