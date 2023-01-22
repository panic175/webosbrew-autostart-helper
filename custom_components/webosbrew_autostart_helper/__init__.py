"""The WebOS Brew Autostart Helper integration."""

from .service import webosbrew_autostart
from homeassistant.core import HomeAssistant, ServiceCall, callback

from .const import DOMAIN


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the WebOS Brew Autostart Helper component."""

    @callback
    async def handle_webosbrew_autostart(call: ServiceCall) -> bool:
        tv_ip = call.data.get("tv_ip")
        result = await webosbrew_autostart(hass, tv_ip)
        return result

    hass.services.async_register(DOMAIN, "webosbrew_autostart_helper", handle_webosbrew_autostart)

    return True
