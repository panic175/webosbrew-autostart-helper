"""Luna Autostart"""
from aiopylgtv import WebOsClient
from typing import Awaitable


async def call_autostart(tvIp: str) -> Awaitable[bool]:
    """Send a luna request to start the WebOsBrew Autostart service."""
    autostart_channel = "org.webosbrew.hbchannel.service/autostart"
    client = await WebOsClient.create(tvIp)
    await client.connect()
    await client.luna_request(autostart_channel, {})
    await client.disconnect()
    return True
