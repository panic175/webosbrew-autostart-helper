import logging
from .utils.call_autostart import (
    call_autostart)
from .utils.get_status import get_status
from .utils.ping import is_available
from .utils.ip_address import is_ip_valid
from homeassistant.core import callback, HomeAssistant

_LOGGER = logging.getLogger(__name__)


@callback
async def webosbrew_autostart(hass: HomeAssistant, tv_ip: str) -> bool:
    _LOGGER.info("IP is set to: %s", tv_ip)
    if not is_ip_valid(tv_ip):
        _LOGGER.error("Invalid IP given: %s", tv_ip)
        return False

    if not is_available(tv_ip):
        _LOGGER.info("TV is offline")
        return False
    status = await get_status(hass, tv_ip)
    if status:
        _LOGGER.info("Autostart already called")
        return False
    _LOGGER.info("Calling autostart")

    try:
        result = await call_autostart(tv_ip)
        _LOGGER.info("Autostart called successfully")
        return result
    except Exception:
        _LOGGER.error("Could not call autostart")
        return False
