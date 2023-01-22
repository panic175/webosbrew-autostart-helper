from requests import get, exceptions
from typing import Awaitable
from homeassistant.core import callback, HomeAssistant


def get_serverinfo_url(ip: str) -> str:
    """Returns the server info url of HyperHDR."""
    return f"http://{ip}:8090/json-rpc?request=%7B%22command%22:%22serverinfo%22%7D"


@callback
async def get_status(hass: HomeAssistant, ip: str) -> Awaitable[bool]:
    """Returns true if the server info url of HyperHDR returns a success"""
    serverinfo_url = get_serverinfo_url(ip)
    try:
        response = await hass.async_add_executor_job(get, serverinfo_url)
        return response.status_code < 400
    except exceptions.RequestException:
        return False
