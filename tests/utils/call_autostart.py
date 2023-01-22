import unittest
from aiopylgtv import WebOsClient
from pytest_homeassistant_custom_component.async_mock import MagicMock, patch
from custom_components.webosbrew_autostart_helper.util.call_autostart import (
    call_autostart,
)


class TestCallAutostart(unittest.TestCase):
    @patch("aiopylgtv.WebOsClient.create")
    async def test_call_autostart(self, mock_create):
        mock_client = MagicMock(spec=WebOsClient)
        mock_create.return_value = mock_client
        result = await call_autostart("192.168.1.100")
        mock_client.connect.assert_called_once()
        mock_client.luna_request.assert_called_with(
            "org.webosbrew.hbchannel.service/autostart", {}
        )
        mock_client.disconnect.assert_called_once()
        self.assertTrue(result)

    @patch("aiopylgtv.WebOsClient.create")
    async def test_call_autostart_error(self, mock_create):
        mock_create.side_effect = Exception("Error connecting to TV")
        with self.assertRaises(Exception):
            await call_autostart("192.168.1.100")
